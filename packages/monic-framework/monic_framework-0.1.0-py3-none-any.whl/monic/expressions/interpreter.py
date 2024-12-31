#
# Monic Framework
#
# Copyright (c) 2024 Cognica, Inc.
#

# pylint: disable=no-else-break,no-else-return,no-else-raise,broad-except
# pylint: disable=too-many-branches,too-many-return-statements,too-many-locals
# pylint: disable=too-many-public-methods,too-many-instance-attributes
# pylint: disable=too-many-statements,too-many-nested-blocks,too-many-lines
# pylint: disable=too-many-arguments
# pylint: disable=unnecessary-dunder-call

import ast
import operator
import time
import types
import typing as t

from dataclasses import dataclass, field

from monic.expressions.context import ExpressionsContext
from monic.expressions.exceptions import (
    SecurityError,
    UnsupportedUnpackingError,
)
from monic.expressions.registry import registry


class ReturnValue(Exception):
    """Raised to return a value from a function."""

    def __init__(self, value):
        self.value = value


@dataclass
class Scope:
    # Names declared as global
    globals: t.Set[str] = field(default_factory=set)
    # Names declared as nonlocal
    nonlocals: t.Set[str] = field(default_factory=set)
    # Names assigned in current scope
    locals: t.Set[str] = field(default_factory=set)


class ScopeContext:
    """Context manager for managing scope stack.

    This context manager ensures that scopes are properly pushed and popped
    from the stack, even if an exception occurs.
    """

    def __init__(
        self,
        interpreter: "ExpressionsInterpreter",
        save_env: bool = False,
    ) -> None:
        self.scope = Scope()
        self.interpreter = interpreter
        self.save_env = save_env

        self.saved_env: dict[str, t.Any] = {}
        self.new_env: dict[str, t.Any] = {}

    def __enter__(self) -> tuple[Scope, dict[str, t.Any] | None]:
        self.interpreter.scope_stack.append(self.scope)
        if self.save_env:
            # Save the current environment
            self.saved_env = self.interpreter.local_env.copy()
            # Create a new environment that inherits from the saved one
            self.new_env = {}
            # Copy over values from outer scope that might be needed
            if len(self.interpreter.scope_stack) > 1:
                outer_scope = self.interpreter.scope_stack[-2]
                for name in outer_scope.locals:
                    if name in self.saved_env:
                        self.new_env[name] = self.saved_env[name]
            self.interpreter.local_env = self.new_env
            return self.scope, self.saved_env
        return self.scope, None

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: types.TracebackType | None,
    ) -> None:
        if self.save_env:
            # Update the saved environment with any changes
            # that should persist outside the with block
            updated_env = {}
            for name, value in self.interpreter.local_env.items():
                if name in self.saved_env:
                    # Keep variables that existed in outer scope
                    updated_env[name] = value
                elif (
                    len(self.interpreter.scope_stack) > 1
                    and name in self.interpreter.scope_stack[-2].locals
                ):
                    # Keep nonlocal variables
                    updated_env[name] = value
            # Restore the saved environment with updates
            self.saved_env.update(updated_env)
            self.interpreter.local_env = self.saved_env
        self.interpreter.scope_stack.pop()


@dataclass
class ControlFlow:
    """Record for tracking control flow state."""

    function_depth: int = 0
    loop_depth: int = 0
    break_flag: bool = False
    continue_flag: bool = False


# Type variable for comprehension result types
T = t.TypeVar("T", list, set)


class ExpressionsInterpreter(ast.NodeVisitor):
    def __init__(self, context: ExpressionsContext | None = None) -> None:
        """Initialize the interpreter.

        Args:
            context: Optional context for execution
        """
        self.started_at = time.monotonic()

        self.context = context or ExpressionsContext()
        self.scope_stack: list[Scope] = [Scope()]  # Track scopes
        self.control: ControlFlow = ControlFlow()

        # Initialize with built-in environment
        self.global_env: dict[str, t.Any] = {
            # Built-in functions
            "print": print,
            "len": len,
            "range": range,
            "abs": abs,
            "min": min,
            "max": max,
            "sum": sum,
            "sorted": sorted,
            "reversed": reversed,
            "zip": zip,
            "enumerate": enumerate,
            "filter": filter,
            "map": map,
            "any": any,
            "all": all,
            "isinstance": isinstance,
            "issubclass": issubclass,
            # Built-in types
            "bool": bool,
            "int": int,
            "float": float,
            "str": str,
            "list": list,
            "tuple": tuple,
            "set": set,
            "dict": dict,
            # Constants
            "None": None,
            "True": True,
            "False": False,
            # Exceptions
            "Exception": Exception,
            "ValueError": ValueError,
            "TypeError": TypeError,
            "NameError": NameError,
            "IndexError": IndexError,
            "KeyError": KeyError,
            "ZeroDivisionError": ZeroDivisionError,
            "StopIteration": StopIteration,
            "TimeoutError": TimeoutError,
            "RuntimeError": RuntimeError,
            "SecurityError": SecurityError,
            "UnsupportedUnpackingError": UnsupportedUnpackingError,
        }

        # Add registered objects to global environment
        self.global_env.update(registry.get_all())

        # Add built-in decorators
        self.global_env.update(
            {
                "classmethod": classmethod,
                "staticmethod": staticmethod,
                "property": property,
            }
        )

        self.local_env: dict[str, t.Any] = {}

        # Initialize last result storage
        self.global_env["_"] = None

        # List of forbidden functions and modules
        self.FORBIDDEN_NAMES = {
            # Built-in functions
            "eval",
            "exec",
            "compile",
            "execfile",
            "open",
            "globals",
            "locals",
            "vars",
            "__import__",
            # Module functions
            "time.sleep",
        }
        # List of forbidden attribute accesses
        self.FORBIDDEN_ATTRS = {
            "__code__",
            "__globals__",
            "__dict__",
            "__class__",
            "__bases__",
            "__subclasses__",
            "__mro__",
            "__qualname__",
        }

    @property
    def current_scope(self) -> Scope:
        return self.scope_stack[-1]

    def execute(self, tree: ast.AST) -> t.Any:
        """Execute an AST."""
        # Perform security check
        self._check_security(tree)

        # Reset the timer for timeout tracking
        self.started_at = time.monotonic()

        try:
            # Handle expression statements specially to capture their value
            if isinstance(tree, ast.Expression):
                result = self.visit(tree)
                self.global_env["_"] = result
                return result
            elif isinstance(tree, ast.Module):
                result = None
                for stmt in tree.body:
                    if isinstance(stmt, ast.Expr):
                        # For expression statements, capture the value
                        result = self.visit(stmt.value)
                        self.global_env["_"] = result
                    else:
                        # For other statements, just execute them
                        self.visit(stmt)
                return result
            else:
                result = self.visit(tree)
                self.global_env["_"] = result
                return result
        except TimeoutError as e:
            raise e
        except Exception as e:
            raise type(e)(str(e)) from e

    def get_name_value(self, name: str) -> t.Any:
        """Get the value of a name in the current scope."""
        return self._get_name_value(name)

    def visit(self, node: ast.AST) -> t.Any:
        """Visit a node and check for timeout."""
        # Check for timeout if one is set
        if self.context.timeout is not None:
            elapsed = time.monotonic() - self.started_at
            if elapsed > self.context.timeout:
                raise TimeoutError(
                    "Execution exceeded timeout of "
                    f"{self.context.timeout} seconds"
                )

        # Get the visitor method for this node type
        visitor = getattr(
            self, f"visit_{type(node).__name__}", self.generic_visit
        )
        return visitor(node)

    def generic_visit(self, node: ast.AST) -> None:
        """Called if no explicit visitor function exists for a node."""
        for _, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        self.visit(item)
            elif isinstance(value, ast.AST):
                self.visit(value)

    def _check_security(self, node: ast.AST) -> None:
        """Check for potentially dangerous operations in the AST.

        Args:
            node: AST node to check

        Raises:
            SecurityError: If dangerous operations are detected
        """
        for op in ast.walk(node):
            # Check for forbidden function calls
            if isinstance(op, ast.Name) and op.id in self.FORBIDDEN_NAMES:
                raise SecurityError(f"Call to builtin '{op.id}' is not allowed")

            # Check for forbidden attribute access
            if isinstance(op, ast.Attribute):
                # Check for direct forbidden attribute access
                if op.attr in self.FORBIDDEN_ATTRS:
                    raise SecurityError(
                        f"Access to '{op.attr}' attribute is not allowed"
                    )

                # Check for forbidden function calls like time.sleep
                if isinstance(op.value, ast.Name):
                    full_name = f"{op.value.id}.{op.attr}"
                    if full_name in self.FORBIDDEN_NAMES:
                        raise SecurityError(
                            f"Call to '{full_name}' is not allowed"
                        )

            # Check for __builtins__ access
            if isinstance(op, ast.Name) and op.id == "__builtins__":
                raise SecurityError(
                    "Access to '__builtins__' attribute is not allowed"
                )

            # Check for import statements
            if isinstance(op, (ast.Import, ast.ImportFrom)):
                raise SecurityError("Import statements are not allowed")

    def visit_Global(self, node: ast.Global) -> None:
        """Handle global declarations."""
        for name in node.names:
            self.current_scope.globals.add(name)
            # Remove from locals if present
            self.current_scope.locals.discard(name)

    def visit_Nonlocal(self, node: ast.Nonlocal) -> None:
        """
        Handle 'nonlocal' statements, e.g.:
            nonlocal x, y

        In Python, if a variable is declared 'nonlocal', it must exist in
        at least one enclosing (function) scope. If not found, raise
        SyntaxError as in the standard Python behavior.
        """
        if len(self.scope_stack) < 2:
            raise SyntaxError(
                "nonlocal declaration not allowed at module level"
            )

        for name in node.names:
            # Mark this name as nonlocal in the current scope
            self.current_scope.nonlocals.add(name)

            found = False
            # Check all outer scopes (excluding the current scope)
            for scope in reversed(self.scope_stack[:-1]):
                # If already local or already marked nonlocal there, consider
                # it found
                if (
                    name in scope.locals
                    or name in scope.nonlocals
                    or name in self.local_env
                ):
                    found = True
                    break

            if not found:
                # If it's not in any enclosing scope, Python raises SyntaxError
                raise SyntaxError(
                    f"No binding for nonlocal '{name}' found in outer scopes"
                )

    def visit_Constant(self, node: ast.Constant) -> t.Any:
        return node.value

    def _get_name_value(self, name: str) -> t.Any:
        """Get value of a name considering scope declarations."""
        # Fast path for common case
        if name in self.local_env:
            return self.local_env[name]

        # Check current scope declarations
        current = self.current_scope
        if name in current.globals:
            if name in self.global_env:
                return self.global_env[name]
            raise NameError(f"Global name '{name}' is not defined")

        if name in current.nonlocals:
            # Use reversed list slice for faster iteration
            for scope in reversed(self.scope_stack[:-1]):
                if name in scope.locals:
                    return self.local_env[name]
            raise NameError(f"Nonlocal name '{name}' is not defined")

        if name in self.global_env:
            return self.global_env[name]

        raise NameError(f"Name '{name}' is not defined")

    def _set_name_value(self, name: str, value: t.Any) -> None:
        """
        Set the value of a name, considering 'global' and 'nonlocal'
        declarations.
        """
        # If declared global in the current scope:
        if name in self.current_scope.globals:
            self.global_env[name] = value
            return

        # If declared nonlocal in the current scope:
        if name in self.current_scope.nonlocals:
            # Walk backward through scopes to find the correct one
            for i in range(len(self.scope_stack) - 2, -1, -1):
                scope = self.scope_stack[i]
                if (
                    name in scope.locals
                    or name in scope.nonlocals
                    or name in self.local_env
                ):
                    # Found the appropriate scope, set value in local_env
                    self.local_env[name] = value
                    return
            raise NameError(f"Nonlocal name '{name}' not found in outer scopes")

        # Otherwise, treat it as a local assignment
        self.current_scope.locals.add(name)
        self.local_env[name] = value

    def _del_name_value(self, name: str) -> None:
        """Delete a name from the appropriate scope."""
        if name == "_":
            raise SyntaxError("Cannot delete special variable '_'")

        if name in self.current_scope.globals:
            if name in self.global_env:
                del self.global_env[name]
            else:
                raise NameError(f"Global name '{name}' is not defined")
        elif name in self.current_scope.nonlocals:
            # Search for name in outer scopes
            found = False
            for scope in reversed(self.scope_stack[:-1]):
                if name in scope.locals:
                    found = True
                    if name in self.local_env:
                        del self.local_env[name]
                        scope.locals.remove(name)
                    break
            if not found:
                raise NameError(f"Nonlocal name '{name}' is not defined")
        else:
            # Try to delete from current scope
            if name in self.current_scope.locals:
                del self.local_env[name]
                self.current_scope.locals.remove(name)
            elif name in self.global_env:
                del self.global_env[name]
            else:
                raise NameError(f"Name '{name}' is not defined")

    def visit_Name(self, node: ast.Name) -> t.Any:
        """Visit a Name node, handling variable lookup according to scope rules.

        Args:
            node: The Name AST node

        Returns:
            The value of the name in the appropriate scope

        Raises:
            NameError: If the name cannot be found in any accessible scope
            SyntaxError: If attempting to modify special variable '_'
            NotImplementedError: If the context type is not supported
        """
        # Handle special underscore variable
        if node.id == "_":
            if isinstance(node.ctx, (ast.Store, ast.Del)):
                op = "delete" if isinstance(node.ctx, ast.Del) else "assign to"
                raise SyntaxError(f"Cannot {op} special variable '_'")
            return self.global_env.get("_")

        # Handle different contexts
        if isinstance(node.ctx, ast.Store):
            return node.id
        elif isinstance(node.ctx, ast.Load):
            # If the name is declared global or nonlocal in the current scope,
            # skip the registry fallback entirely so we preserve the correct
            # error.
            if (
                node.id in self.current_scope.globals
                or node.id in self.current_scope.nonlocals
            ):
                return self._get_name_value(node.id)

            try:
                return self._get_name_value(node.id)
            except NameError:
                # If not found in current scope, try the registry
                try:
                    return registry.get(node.id)
                except KeyError as e:
                    raise NameError(f"Name '{node.id}' is not defined") from e
        elif isinstance(node.ctx, ast.Del):
            self._del_name_value(node.id)
        else:
            raise NotImplementedError(
                f"Unsupported context type: {type(node.ctx).__name__}"
            )

    _AUG_OP_MAP: t.Dict[t.Type[ast.operator], t.Callable] = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
        ast.BitAnd: operator.and_,
        ast.BitOr: operator.or_,
        ast.BitXor: operator.xor,
        ast.LShift: operator.lshift,
        ast.RShift: operator.rshift,
    }

    def visit_AugAssign(self, node: ast.AugAssign) -> None:
        """Handle augmented assignment with proper scope handling."""
        op_func = self._AUG_OP_MAP.get(type(node.op))
        if not op_func:
            raise NotImplementedError(
                "Unsupported augmented assignment operator: "
                f"{type(node.op).__name__}"
            )

        # Get the current value
        if isinstance(node.target, ast.Name):
            target_value = self._get_name_value(node.target.id)
        elif isinstance(node.target, ast.Attribute):
            obj = self.visit(node.target.value)
            target_value = getattr(obj, node.target.attr)
        elif isinstance(node.target, ast.Subscript):
            container = self.visit(node.target.value)
            index = self.visit(node.target.slice)
            target_value = container[index]
        else:
            raise NotImplementedError(
                "Unsupported augmented assignment target: "
                f"{type(node.target).__name__}"
            )

        # Compute the new value
        right_value = self.visit(node.value)
        result = op_func(target_value, right_value)

        # Store the result
        if isinstance(node.target, ast.Name):
            self._set_name_value(node.target.id, result)
        elif isinstance(node.target, ast.Attribute):
            setattr(obj, node.target.attr, result)
        elif isinstance(node.target, ast.Subscript):
            container[index] = result

    def visit_Assign(self, node: ast.Assign) -> None:
        value = self.visit(node.value)
        # Handle multiple targets
        if len(node.targets) > 1:
            # Multiple target assignment: a = b = 10
            for target in node.targets:
                self._handle_unpacking_target(target, value)
        else:
            # Single target assignment
            target = node.targets[0]
            self._handle_unpacking_target(target, value)

    def _handle_name_target(self, target: ast.Name, value: t.Any) -> None:
        """Handle simple name assignment with scope handling.

        Args:
            target: Name AST node
            value: Value to assign
        """
        self._set_name_value(target.id, value)

    def _handle_attribute_target(
        self, target: ast.Attribute, value: t.Any
    ) -> None:
        """Handle attribute assignment (e.g., self.x = value).

        Args:
            target: Attribute AST node
            value: Value to assign
        """
        obj = self.visit(target.value)
        setattr(obj, target.attr, value)

    def _handle_subscript_target(
        self, target: ast.Subscript, value: t.Any
    ) -> None:
        """Handle subscript assignment (e.g., lst[0] = value).

        Args:
            target: Subscript AST node
            value: Value to assign
        """
        container = self.visit(target.value)
        index = self.visit(target.slice)
        container[index] = value

    def _handle_unpacking_target(self, target: ast.AST, value: t.Any) -> None:
        """Handle different types of unpacking targets.

        Args:
            target: AST node representing the unpacking target
            value: The value being assigned

        Raises:
            UnsupportedUnpackingError: If an unsupported unpacking pattern is
            encountered
        """
        if isinstance(target, ast.Name):
            self._handle_name_target(target, value)
        elif isinstance(target, ast.Attribute):
            self._handle_attribute_target(target, value)
        elif isinstance(target, ast.Subscript):
            self._handle_subscript_target(target, value)
        elif isinstance(target, (ast.Tuple, ast.List)):
            self._handle_sequence_unpacking(target, value)
        else:
            raise UnsupportedUnpackingError(
                f"Unsupported unpacking target type: {type(target).__name__}"
            )

    def _handle_sequence_unpacking(
        self,
        target: ast.Tuple | ast.List,
        value: t.Any,
    ) -> None:
        """Handle sequence (tuple/list) unpacking.

        Args:
            target: Tuple or List AST node
            value: Value to unpack

        Raises:
            ValueError: If value cannot be unpacked
            UnsupportedUnpackingError: If unpacking pattern is not supported
        """
        with ScopeContext(self):
            try:
                if not hasattr(value, "__iter__"):
                    raise ValueError("Cannot unpack non-iterable value")

                # Check for starred expressions (extended unpacking)
                starred_indices = [
                    i
                    for i, elt in enumerate(target.elts)
                    if isinstance(elt, ast.Starred)
                ]

                if len(starred_indices) > 1:
                    raise UnsupportedUnpackingError(
                        "Cannot use multiple starred expressions in assignment"
                    )

                if starred_indices:
                    # Handle starred unpacking
                    star_index = starred_indices[0]
                    starred_target = t.cast(
                        ast.Starred, target.elts[star_index]
                    )
                    self._handle_starred_unpacking(
                        target.elts, value, star_index, starred_target
                    )
                else:
                    # Standard unpacking without starred expression
                    value_list = list(value)
                    if len(value_list) < len(target.elts):
                        raise ValueError("Not enough values to unpack")
                    elif len(value_list) > len(target.elts):
                        raise ValueError("Too many values to unpack")

                    # Unpack each element
                    for tgt, val in zip(target.elts, value):
                        self._handle_unpacking_target(tgt, val)
            except (TypeError, ValueError) as e:
                raise UnsupportedUnpackingError(str(e)) from e

    def _handle_starred_unpacking(
        self,
        target_elts: list[ast.expr],
        value: t.Any,
        star_index: int,
        starred_target: ast.Starred,
    ) -> None:
        """Handle starred unpacking in sequence assignments.

        Args:
            target_elts: List of target elements
            value: Value being unpacked
            star_index: Index of the starred expression
            starred_target: The starred target node

        Raises:
            ValueError: If there are not enough values to unpack
            UnsupportedUnpackingError: If unpacking pattern is not supported
        """
        with ScopeContext(self):
            iter_value = iter(value)

            # Handle elements before the starred expression
            before_elements = target_elts[:star_index]
            for tgt in before_elements:
                try:
                    self._handle_unpacking_target(tgt, next(iter_value))
                except StopIteration as e:
                    raise ValueError("Not enough values to unpack") from e

            # Collect remaining elements for the starred target
            starred_values = list(iter_value)

            # Calculate how many elements should be in the starred part
            after_star_count = len(target_elts) - star_index - 1

            # If there are more elements after the starred part
            if after_star_count > 0:
                # Make sure there are enough elements
                if len(starred_values) < after_star_count:
                    raise ValueError("Not enough values to unpack")

                # Separate starred values
                starred_list = starred_values[:-after_star_count]
                after_star_values = starred_values[-after_star_count:]

                # Assign starred target
                if isinstance(starred_target.value, ast.Name):
                    self._set_name_value(starred_target.value.id, starred_list)

                # Assign elements after starred
                after_elements = target_elts[star_index + 1 :]
                for tgt, val in zip(after_elements, after_star_values):
                    self._handle_unpacking_target(tgt, val)
            else:
                # If no elements after starred, just assign the rest
                # to the starred target
                if isinstance(starred_target.value, ast.Name):
                    self._set_name_value(
                        starred_target.value.id, starred_values
                    )

    def visit_NamedExpr(self, node: ast.NamedExpr) -> t.Any:
        """Handle named expressions (walrus operator).

        Example: (x := 1) assigns 1 to x and returns 1
        """
        value = self.visit(node.value)

        # The target should be a Name node
        if not isinstance(node.target, ast.Name):
            raise SyntaxError("Invalid target for named expression")

        # Named expressions bind in the containing scope
        if len(self.scope_stack) > 1:
            # If we're in a nested scope, add to the parent scope
            parent_scope = self.scope_stack[-2]
            parent_scope.locals.add(node.target.id)
        else:
            # In the global scope, add to current scope
            self.current_scope.locals.add(node.target.id)

        # Set the value in the current environment
        self.local_env[node.target.id] = value
        return value

    def visit_BoolOp(self, node: ast.BoolOp) -> t.Any:
        """Handle logical AND and OR with Python's short-circuit behavior."""
        if isinstance(node.op, ast.And):
            # "and" should return the first falsy value, or the last value if
            # all are truthy
            result = True
            for value_node in node.values:
                result = self.visit(value_node)
                if not result:
                    return result  # Short-circuit on falsy
            return result
        elif isinstance(node.op, ast.Or):
            # "or" should return the first truthy value, or the last value if
            # all are falsy
            result = False
            for value_node in node.values:
                result = self.visit(value_node)
                if result:
                    return result  # Short-circuit on truthy
            return result
        else:
            raise NotImplementedError(
                f"Unsupported BoolOp operator: {type(node.op).__name__}"
            )

    def visit_UnaryOp(self, node: ast.UnaryOp) -> t.Any:
        operand = self.visit(node.operand)

        if isinstance(node.op, ast.UAdd):
            return +operand
        elif isinstance(node.op, ast.USub):
            return -operand
        elif isinstance(node.op, ast.Not):
            return not operand
        elif isinstance(node.op, ast.Invert):
            return ~operand
        else:
            raise NotImplementedError(
                f"Unsupported unary operator: {type(node.op).__name__}"
            )

    def visit_BinOp(self, node: ast.BinOp) -> t.Any:
        left = self.visit(node.left)
        right = self.visit(node.right)

        try:
            if isinstance(node.op, ast.Add):
                return left + right
            elif isinstance(node.op, ast.Sub):
                return left - right
            elif isinstance(node.op, ast.Mult):
                return left * right
            elif isinstance(node.op, ast.Div):
                return left / right
            elif isinstance(node.op, ast.FloorDiv):
                return left // right
            elif isinstance(node.op, ast.Mod):
                return left % right
            elif isinstance(node.op, ast.Pow):
                return left**right
            else:
                raise NotImplementedError(
                    f"Unsupported binary operator: {type(node.op).__name__}"
                )
        except (ZeroDivisionError, TypeError, ValueError) as e:
            raise type(e)(str(e)) from e

    _COMPARE_OP_MAP: t.Dict[t.Type[ast.cmpop], t.Callable] = {
        ast.Eq: operator.eq,
        ast.NotEq: operator.ne,
        ast.Lt: operator.lt,
        ast.LtE: operator.le,
        ast.Gt: operator.gt,
        ast.GtE: operator.ge,
        ast.In: lambda x, y: x in y,
        ast.NotIn: lambda x, y: x not in y,
        ast.Is: operator.is_,
        ast.IsNot: operator.is_not,
    }

    def visit_Compare(self, node: ast.Compare) -> bool:
        try:
            left = self.visit(node.left)

            for op, comparator in zip(node.ops, node.comparators):
                right = self.visit(comparator)
                op_func = self._COMPARE_OP_MAP.get(type(op))
                if op_func is None:
                    raise NotImplementedError(
                        f"Unsupported comparison operator: {type(op).__name__}"
                    )

                if not op_func(left, right):
                    return False
                left = right

            return True
        except TypeError as e:
            raise TypeError(f"Invalid comparison: {str(e)}") from e

    def visit_Try(self, node: ast.Try) -> None:
        """Handle try-except-else-finally statements.

        Args:
            node: Try AST node
        """
        with ScopeContext(self):
            try:
                for stmt in node.body:
                    self.visit(stmt)
            except Exception as e:
                handled = False
                for handler in node.handlers:
                    if handler.type is None:
                        exc_class = Exception
                    else:
                        exc_class = self._get_exception_class(handler.type)

                    if isinstance(e, exc_class):
                        handled = True
                        if handler.name is not None:
                            self.local_env[handler.name] = e
                        for stmt in handler.body:
                            self.visit(stmt)
                        if handler.name is not None:
                            del self.local_env[handler.name]
                        break

                if not handled:
                    raise e
            else:
                if node.orelse:
                    for stmt in node.orelse:
                        self.visit(stmt)
            finally:
                if node.finalbody:
                    for stmt in node.finalbody:
                        self.visit(stmt)

    def _get_exception_class(self, node: ast.expr) -> t.Type[Exception]:
        if isinstance(node, ast.Name):
            class_name = node.id
            if class_name in globals()["__builtins__"]:
                exc_class = globals()["__builtins__"][class_name]
                if isinstance(exc_class, type) and issubclass(
                    exc_class, Exception
                ):
                    return exc_class
            raise NameError(
                f"Name '{class_name}' is not defined or is not an exception "
                "class"
            )
        elif isinstance(node, ast.Attribute):
            value = self.visit(node.value)
            attr = node.attr
            if hasattr(value, attr):
                exc_class = getattr(value, attr)
                if isinstance(exc_class, type) and issubclass(
                    exc_class, Exception
                ):
                    return exc_class
            raise NameError(f"'{attr}' is not a valid exception class")
        else:
            raise TypeError(
                f"Invalid exception class specification: {ast.dump(node)}"
            )

    def visit_Raise(self, node: ast.Raise) -> None:
        if node.exc is None:
            raise RuntimeError("No active exception to re-raise")

        exc = self.visit(node.exc)
        if isinstance(exc, type) and issubclass(exc, Exception):
            if node.cause:
                cause = self.visit(node.cause)
                raise exc from cause
            raise exc()
        else:
            if isinstance(exc, BaseException):
                raise exc
            else:
                raise TypeError(
                    f"Expected an exception instance, got {type(exc).__name__}"
                )

    def visit_With(self, node: ast.With) -> None:
        """
        Execute a with statement, properly handling scopes and context managers.
        """
        # Create a new scope for the with block
        scope = Scope()

        # Save the current environment
        outer_env = self.local_env

        # Create a new environment for the with block
        self.local_env = {}
        # Copy only non-local variables from outer environment
        for name, value in outer_env.items():
            if name not in scope.locals:
                self.local_env[name] = value

        self.scope_stack.append(scope)

        try:
            # List to track context managers and their values
            context_managers = []

            try:
                # Enter all context managers in order
                for item in node.items:
                    try:
                        # Evaluate the context manager expression using outer
                        # environment
                        prev_env = self.local_env
                        self.local_env = outer_env
                        try:
                            context_manager = self.visit(item.context_expr)
                        finally:
                            self.local_env = prev_env

                        try:
                            # Enter the context manager
                            value = context_manager.__enter__()
                            context_managers.append((context_manager, value))

                            # Handle the optional 'as' variable if present
                            if item.optional_vars is not None:
                                # Add the 'as' variable to the with block's
                                # environment
                                name = self.visit(item.optional_vars)
                                self.local_env[name] = value
                                scope.locals.add(name)
                        except Exception as enter_exc:
                            # If __enter__ fails, properly clean up previous
                            # context managers
                            for mgr, _ in reversed(context_managers[:-1]):
                                try:
                                    mgr.__exit__(None, None, None)
                                except Exception:
                                    # Ignore any cleanup exceptions
                                    pass
                            raise enter_exc
                    except Exception as ctx_exc:
                        # Clean up any successfully entered context managers
                        self._exit_context_managers(context_managers, ctx_exc)
                        raise ctx_exc

                try:
                    # Execute the body of the with statement
                    for stmt in node.body:
                        self.visit(stmt)
                        # Track any new variables defined in the body
                        if isinstance(stmt, ast.Assign):
                            for target in stmt.targets:
                                if isinstance(target, ast.Name):
                                    scope.locals.add(target.id)
                except Exception as body_exc:
                    # Handle any exception from the body
                    if not self._exit_context_managers(
                        context_managers, body_exc
                    ):
                        raise body_exc
                else:
                    # No exception occurred, exit context managers normally
                    self._exit_context_managers(context_managers, None)
            finally:
                # Update outer environment with modified variables
                for name, value in self.local_env.items():
                    if name in outer_env:  # Only update existing variables
                        outer_env[name] = value

                # Restore the outer environment
                self.local_env = outer_env
        finally:
            # Pop the scope
            self.scope_stack.pop()

    def _exit_context_managers(
        self,
        context_managers: list[tuple[t.Any, t.Any]],
        exc_info: t.Optional[Exception],
    ) -> bool:
        """Exit a list of context managers, handling any exceptions.

        Args:
            context_managers: List of (context_manager, value) pairs to exit
            exc_info: The exception that occurred, if any

        Returns:
            bool: True if any context manager suppressed the exception
        """
        # Track if any context manager suppresses the exception
        suppressed = False

        if exc_info is not None:
            exc_type = type(exc_info)
            exc_value = exc_info
            exc_tb = exc_info.__traceback__
        else:
            exc_type = None
            exc_value = None
            exc_tb = None

        # Exit context managers in reverse order
        for cm, _ in reversed(context_managers):
            try:
                if cm.__exit__(exc_type, exc_value, exc_tb):
                    suppressed = True
                    exc_type = None
                    exc_value = None
                    exc_tb = None
            except Exception as exit_exc:
                # If __exit__ raises an exception, update the exception info
                exc_type = type(exit_exc)
                exc_value = exit_exc
                exc_tb = exit_exc.__traceback__
                suppressed = False

        return suppressed

    def visit_If(self, node: ast.If) -> None:
        if self.visit(node.test):
            for stmt in node.body:
                self.visit(stmt)
        elif node.orelse:
            for stmt in node.orelse:
                self.visit(stmt)

    def visit_IfExp(self, node: ast.IfExp) -> t.Any:
        # Ternary expression: <body> if <test> else <orelse>
        condition = self.visit(node.test)
        if condition:
            return self.visit(node.body)
        else:
            return self.visit(node.orelse)

    def visit_Pass(
        self, node: ast.Pass  # pylint: disable=unused-argument
    ) -> None:
        """
        Handle the Pass statement.

        The Pass statement is a no-operation statement that does nothing.
        It's used as a placeholder when syntactically a statement is required
        but no action is desired.

        Args:
            node (ast.Pass): The Pass statement AST node

        Returns:
            None
        """
        # Do nothing, which is exactly what Pass is supposed to do
        return None

    def visit_Break(
        self, node: ast.Break  # pylint: disable=unused-argument
    ) -> None:
        """Handle break statement."""
        if self.control.loop_depth == 0:
            raise SyntaxError("'break' outside loop")
        self.control.break_flag = True

    def visit_Continue(
        self, node: ast.Continue  # pylint: disable=unused-argument
    ) -> None:
        """Handle continue statement."""
        if self.control.loop_depth == 0:
            raise SyntaxError("'continue' outside loop")
        self.control.continue_flag = True

    def visit_While(self, node: ast.While) -> None:
        self.control.loop_depth += 1

        try:
            while True:
                test_result = self.visit(node.test)  # Evaluate test first
                if not test_result:
                    break

                try:
                    for stmt in node.body:
                        self.visit(stmt)
                        if self.control.break_flag:
                            break
                        if self.control.continue_flag:
                            self.control.continue_flag = False
                            break
                    if self.control.break_flag:
                        break
                    else:
                        # This else block is executed if no break occurred
                        continue
                except ReturnValue as rv:
                    raise rv
                except Exception as e:
                    if node.orelse:
                        for stmt in node.orelse:
                            self.visit(stmt)
                    raise e
        finally:
            self.control.break_flag = False
            self.control.continue_flag = False
            self.control.loop_depth -= 1

    def visit_For(self, node: ast.For) -> None:
        self.control.loop_depth += 1

        iter_value = self.visit(node.iter)

        try:
            for item in iter_value:
                # Use the unpacking method to handle the target
                self._handle_unpacking_target(node.target, item)

                try:
                    for stmt in node.body:
                        self.visit(stmt)
                        if self.control.break_flag:
                            break
                        if self.control.continue_flag:
                            self.control.continue_flag = False
                            break
                    if self.control.break_flag:
                        break
                    else:
                        # This else block is executed if no break occurred
                        continue
                except ReturnValue as rv:
                    raise rv
            if not self.control.break_flag and node.orelse:
                for stmt in node.orelse:
                    self.visit(stmt)
        except Exception as e:
            if node.orelse:
                for stmt in node.orelse:
                    self.visit(stmt)
            raise e
        finally:
            self.control.break_flag = False
            self.control.continue_flag = False
            self.control.loop_depth -= 1

    def _validate_nonlocal_declarations(
        self, body: t.Sequence[ast.stmt], scope_stack: list[Scope]
    ) -> None:
        """Validate nonlocal declarations in function body.

        Args:
            body: Function body AST nodes
            scope_stack: Current scope stack

        Raises:
            SyntaxError: If nonlocal declaration is invalid
        """
        for stmt in body:
            if isinstance(stmt, ast.Nonlocal):
                if len(scope_stack) < 2:
                    raise SyntaxError(
                        "nonlocal declaration not allowed at module level"
                    )

                # For non-nested functions, check bindings at definition time
                if len(scope_stack) == 2:  # Only one outer scope
                    for name in stmt.names:
                        found = False
                        # Check all outer scopes (excluding the current scope)
                        for scope in reversed(scope_stack[:-1]):
                            if (
                                name in scope.locals
                                or name in scope.nonlocals
                                or name in self.local_env
                            ):
                                found = True
                                break
                        if not found:
                            raise SyntaxError(
                                f"No binding for nonlocal '{name}' found "
                                "in outer scopes"
                            )

    def _process_function_parameters(
        self,
        func_name: str,
        call_args: tuple[t.Any, ...],
        call_kwargs: dict[str, t.Any],
        positional_params: list[ast.arg],
        defaults: list[t.Any],
        required_count: int,
        kwonly_params: list[ast.arg],
        kw_defaults: list[t.Any | None],
        vararg: ast.arg | None,
        kwarg: ast.arg | None,
    ) -> None:
        """Process and bind function parameters to arguments.

        Args:
            func_name: Name of the function being called
            call_args: Positional arguments tuple
            call_kwargs: Keyword arguments dictionary
            positional_params: List of positional parameter AST nodes
            defaults: List of default values for positional parameters
            required_count: Number of required positional parameters
            kwonly_params: List of keyword-only parameter AST nodes
            kw_defaults: List of default values for keyword-only parameters
            vararg: *args parameter AST node if present
            kwarg: **kwargs parameter AST node if present

        Raises:
            TypeError: If argument binding fails
        """
        # 1) Bind positional
        bound_args_count = min(len(call_args), len(positional_params))
        for i in range(bound_args_count):
            param = positional_params[i]
            self._set_name_value(param.arg, call_args[i])

        # leftover positional -> defaults or error
        for i in range(bound_args_count, len(positional_params)):
            param = positional_params[i]
            param_name = param.arg

            if i < required_count:
                # This param must be provided either by leftover call_args
                # (already exhausted) or by a keyword
                if param_name in call_kwargs:
                    self._set_name_value(
                        param_name, call_kwargs.pop(param_name)
                    )
                else:
                    raise TypeError(
                        f"{func_name}() missing required positional argument: "
                        f"'{param_name}'"
                    )
            else:
                # This param has a default
                default_index = i - required_count
                if param_name in call_kwargs:
                    # Use the user-provided keyword
                    self._set_name_value(
                        param_name, call_kwargs.pop(param_name)
                    )
                else:
                    # Use the default
                    self._set_name_value(param_name, defaults[default_index])

        # 2) Handle keyword-only params
        for i, kw_param in enumerate(kwonly_params):
            pname = kw_param.arg
            if pname in call_kwargs:
                self._set_name_value(pname, call_kwargs.pop(pname))
            else:
                # if there's a default => use it; else error
                if kw_defaults[i] is not None:
                    self._set_name_value(pname, kw_defaults[i])
                else:
                    raise TypeError(
                        f"{func_name}() missing required keyword-only "
                        f"argument: '{pname}'"
                    )

        # 3) Handle *args
        if vararg:
            vararg_name = vararg.arg
            leftover = call_args[len(positional_params) :]
            self._set_name_value(vararg_name, leftover)
        else:
            # If no vararg, but user gave extra positional => error
            if len(call_args) > len(positional_params):
                raise TypeError(
                    f"{func_name}() takes {len(positional_params)} positional "
                    f"arguments but {len(call_args)} were given"
                )

        # 4) Handle **kwargs
        if kwarg:
            kwarg_name = kwarg.arg
            self._set_name_value(kwarg_name, call_kwargs)
        else:
            if call_kwargs:
                first_unexpected = next(iter(call_kwargs))
                raise TypeError(
                    f"{func_name}() got an unexpected keyword argument: "
                    f"'{first_unexpected}'"
                )

    def _create_function_closure(
        self,
        func_def: ast.FunctionDef,
        outer_env: dict[str, t.Any],
        closure_env: dict[str, t.Any],
        defaults: list[t.Any],
        kw_defaults: list[t.Any | None],
        required_count: int,
    ) -> t.Callable[..., t.Any]:
        """Create a closure for the function definition."""

        def func(*call_args, **call_kwargs):
            # Create a new execution scope
            func_scope = Scope()
            self.scope_stack.append(func_scope)

            prev_env = self.local_env
            # Build local env from outer + closure
            self.local_env = {**outer_env, **closure_env}

            self.control.function_depth += 1

            try:
                # Register the function name itself for recursion
                self.local_env[func_def.name] = func

                # Process nonlocal declarations at function execution time
                for stmt in func_def.body:
                    if isinstance(stmt, ast.Nonlocal):
                        for name in stmt.names:
                            found = False
                            # Check all outer scopes
                            # (excluding the current scope)
                            for scope in reversed(self.scope_stack[:-1]):
                                if (
                                    name in scope.locals
                                    or name in scope.nonlocals
                                    or name in self.local_env
                                ):
                                    found = True
                                    break
                            if not found:
                                raise SyntaxError(
                                    f"No binding for nonlocal '{name}' found "
                                    "in outer scopes"
                                )
                            # Mark this name as nonlocal in the current scope
                            self.current_scope.nonlocals.add(name)

                # Process function parameters
                self._process_function_parameters(
                    func_def.name,
                    call_args,
                    call_kwargs,
                    func_def.args.args,
                    defaults,
                    required_count,
                    func_def.args.kwonlyargs,
                    kw_defaults,
                    func_def.args.vararg,
                    func_def.args.kwarg,
                )

                # Execute function body
                try:
                    for stmt in func_def.body:
                        self.visit(stmt)
                    return None
                except ReturnValue as rv:
                    return rv.value
            finally:
                self.control.function_depth -= 1

                # Update nonlocals
                for name in func_scope.nonlocals:
                    if name in self.local_env:
                        closure_env[name] = self.local_env[name]
                        outer_env[name] = self.local_env[name]

                self.local_env = prev_env
                self.scope_stack.pop()

        return func

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """
        Handle function definition with support for named parameters, defaults,
        keyword-only, *args, and **kwargs.
        """
        def_scope = Scope()
        self.scope_stack.append(def_scope)

        try:
            # Validate nonlocal declarations at function definition time
            self._validate_nonlocal_declarations(node.body, self.scope_stack)

            closure_env: t.Dict[str, t.Any] = {}
            outer_env: t.Dict[str, t.Any] = self.local_env

            # Precompute default values for positional and kw-only
            defaults = [self.visit(d) for d in node.args.defaults]
            kw_defaults = [
                None if d is None else self.visit(d)
                for d in node.args.kw_defaults
            ]

            # e.g. if we have 3 positional params and 1 default then
            # required_count=2
            required_count = len(node.args.args) - len(defaults)

            # Create the function closure
            func = self._create_function_closure(
                func_def=node,
                outer_env=outer_env,
                closure_env=closure_env,
                defaults=defaults,
                kw_defaults=kw_defaults,
                required_count=required_count,
            )

            # Register the function in the current scope
            self._set_name_value(node.name, func)
        finally:
            self.scope_stack.pop()

    def _create_lambda_closure(
        self,
        node: ast.Lambda,
        outer_env: dict[str, t.Any],
        closure_env: dict[str, t.Any],
        defaults: list[t.Any],
        kw_defaults: list[t.Any | None],
        required_count: int,
    ) -> t.Callable[..., t.Any]:
        """Create a closure for the lambda function.

        Args:
            node: Lambda AST node
            outer_env: Outer environment dictionary
            closure_env: Closure environment dictionary
            defaults: List of default values for positional parameters
            kw_defaults: List of default values for keyword-only parameters
            required_count: Number of required positional parameters

        Returns:
            The created lambda closure
        """

        def lambda_func(*call_args, **call_kwargs):
            lambda_scope = Scope()
            self.scope_stack.append(lambda_scope)

            prev_env = self.local_env
            self.local_env = {**outer_env, **closure_env}

            try:
                # Process function parameters
                self._process_function_parameters(
                    "<lambda>",
                    call_args,
                    call_kwargs,
                    node.args.args,
                    defaults,
                    required_count,
                    node.args.kwonlyargs,
                    kw_defaults,
                    node.args.vararg,
                    node.args.kwarg,
                )

                # Evaluate the body
                result = self.visit(node.body)

                # Update nonlocals
                for name in lambda_scope.nonlocals:
                    if name in self.local_env:
                        closure_env[name] = self.local_env[name]
                        outer_env[name] = self.local_env[name]

                return result
            finally:
                self.local_env = prev_env
                self.scope_stack.pop()

        return lambda_func

    def visit_Lambda(self, node: ast.Lambda) -> t.Callable[..., t.Any]:
        """Handle lambda function definition.

        Args:
            node: Lambda AST node

        Returns:
            The created lambda function
        """
        closure_env: dict[str, t.Any] = {}
        outer_env: dict[str, t.Any] = self.local_env

        # Precompute default values for positional and kw-only
        defaults = [self.visit(d) for d in node.args.defaults]
        kw_defaults = [
            None if d is None else self.visit(d) for d in node.args.kw_defaults
        ]
        required_count = len(node.args.args) - len(defaults)

        # Create the lambda closure
        return self._create_lambda_closure(
            node=node,
            outer_env=outer_env,
            closure_env=closure_env,
            defaults=defaults,
            kw_defaults=kw_defaults,
            required_count=required_count,
        )

    def visit_Return(self, node: ast.Return) -> None:
        if self.control.function_depth == 0:
            raise SyntaxError("'return' outside function")

        value = None if node.value is None else self.visit(node.value)
        raise ReturnValue(value)

    def _evaluate_call_arguments(
        self, args: list[ast.expr], keywords: list[ast.keyword]
    ) -> tuple[list[t.Any], dict[str, t.Any]]:
        """Evaluate function call arguments.

        Args:
            args: List of positional argument AST nodes
            keywords: List of keyword argument AST nodes

        Returns:
            Tuple of (positional args list, keyword args dict)

        Raises:
            TypeError: If keyword argument is invalid
        """
        # Evaluate positional arguments
        pos_args = [self.visit(arg) for arg in args]

        # Evaluate keyword arguments
        kwargs = {}
        for kw in keywords:
            if kw.arg is None:
                # This is the case of f(**some_dict)
                dict_val = self.visit(kw.value)
                if not isinstance(dict_val, dict):
                    raise TypeError(
                        "Argument after ** must be a dict, got "
                        f"{type(dict_val).__name__}"
                    )
                # Merge into our kwargs
                for k, v in dict_val.items():
                    if not isinstance(k, str):
                        raise TypeError("Keywords must be strings")
                    kwargs[k] = v
            else:
                # Normal keyword argument f(key=value)
                key_name = kw.arg
                value = self.visit(kw.value)
                kwargs[key_name] = value

        return pos_args, kwargs

    def _call_function(
        self, func: t.Any, pos_args: list[t.Any], kwargs: dict[str, t.Any]
    ) -> t.Any:
        """Call a function with the given arguments.

        Args:
            func: Function object to call
            pos_args: List of positional arguments
            kwargs: Dictionary of keyword arguments

        Returns:
            Result of the function call

        Raises:
            TypeError: If the function is not callable
        """
        # Check if the function is callable
        if not callable(func):
            raise TypeError(f"'{type(func).__name__}' object is not callable")

        # Handle registered functions
        if registry.is_registered(func):
            return func(*pos_args, **kwargs)

        # Handle bound methods
        if isinstance(func, types.MethodType):
            return func(*pos_args, **kwargs)

        # Handle normal functions
        return func(*pos_args, **kwargs)

    def visit_Call(self, node: ast.Call) -> t.Any:
        """
        Handle function calls, including positional args, keyword args, and
        **kwargs.

        Args:
            node: Call AST node

        Returns:
            Result of the function call

        Raises:
            TypeError: If the function is not callable or arguments are invalid
        """
        # Evaluate the function object
        func = self.visit(node.func)

        # Evaluate arguments
        pos_args, kwargs = self._evaluate_call_arguments(
            node.args, node.keywords
        )

        # Call the function
        return self._call_function(func, pos_args, kwargs)

    def visit_GeneratorExp(
        self, node: ast.GeneratorExp
    ) -> t.Generator[t.Any, None, None]:
        """Handle generator expressions."""
        # Create new scope for the generator expression
        gen_scope = Scope()
        self.scope_stack.append(gen_scope)

        # Copy the outer environment
        outer_env = self.local_env
        self.local_env = outer_env.copy()

        try:

            def generator() -> t.Generator[t.Any, None, None]:
                def process_generator(
                    generators: list, index: int = 0
                ) -> t.Generator[t.Any, None, None]:
                    if index >= len(generators):
                        # Base case: all generators processed, yield element
                        value = self.visit(node.elt)
                        yield value
                        return

                    generator = generators[index]
                    iter_obj = self.visit(generator.iter)

                    # Save the current environment before processing this
                    # generator
                    current_env = self.local_env.copy()

                    for item in iter_obj:
                        # Restore environment from before this generator's loop
                        self.local_env = current_env.copy()

                        try:
                            self._handle_unpacking_target(
                                generator.target, item
                            )
                        except UnsupportedUnpackingError:
                            if isinstance(generator.target, ast.Name):
                                self._set_name_value(generator.target.id, item)
                            else:
                                raise

                        # Check if conditions
                        if all(
                            self.visit(if_clause) for if_clause in generator.ifs
                        ):
                            # Process next generator or yield result
                            yield from process_generator(generators, index + 1)

                        # Update outer environment with any named expression
                        # bindings
                        for name, value in self.local_env.items():
                            if name not in current_env:
                                outer_env[name] = value

                # Start processing generators recursively
                yield from process_generator(node.generators)

            return generator()
        finally:
            # Restore the outer environment and pop the scope
            self.local_env = outer_env
            self.scope_stack.pop()

    def visit_List(self, node: ast.List) -> list:
        return [self.visit(elt) for elt in node.elts]

    def visit_Tuple(self, node: ast.Tuple) -> tuple:
        return tuple(self.visit(elt) for elt in node.elts)

    def visit_Set(self, node: ast.Set) -> set:
        return {self.visit(elt) for elt in node.elts}

    def visit_Dict(self, node: ast.Dict) -> dict:
        return {
            self.visit(key) if key is not None else None: self.visit(value)
            for key, value in zip(node.keys, node.values)
        }

    def _setup_comprehension_scope(self) -> tuple[Scope, dict[str, t.Any]]:
        """Set up a new scope for comprehension execution.

        Returns:
            Tuple of (new scope, outer environment)
        """
        # Create new scope for the comprehension
        comp_scope = Scope()
        self.scope_stack.append(comp_scope)

        # Copy the outer environment
        outer_env = self.local_env
        self.local_env = outer_env.copy()

        return comp_scope, outer_env

    def _process_generator_item(
        self,
        generator: ast.comprehension,
        item: t.Any,
        current_env: dict[str, t.Any],
        outer_env: dict[str, t.Any],
    ) -> bool:
        """Process a single item in a generator.

        Args:
            generator: Generator AST node
            item: Current item being processed
            current_env: Current environment dictionary
            outer_env: Outer environment dictionary

        Returns:
            bool: Whether all conditions are met

        Raises:
            UnsupportedUnpackingError: If target unpacking fails
        """
        # Restore environment from before this generator's loop
        self.local_env = current_env.copy()

        try:
            self._handle_unpacking_target(generator.target, item)
        except UnsupportedUnpackingError:
            if isinstance(generator.target, ast.Name):
                self._set_name_value(generator.target.id, item)
            else:
                raise

        # Check if all conditions are met
        conditions_met = all(
            self.visit(if_clause) for if_clause in generator.ifs
        )

        # Update outer environment with any named expression bindings
        for name, value in self.local_env.items():
            if name not in current_env:
                outer_env[name] = value

        return conditions_met

    def _handle_comprehension(
        self, node: ast.ListComp | ast.SetComp, result_type: type[T]
    ) -> T:
        """Handle list and set comprehensions.

        Args:
            node: ListComp or SetComp AST node
            result_type: Type of the result (list or set)

        Returns:
            The evaluated comprehension result
        """
        _, outer_env = self._setup_comprehension_scope()

        try:
            result: list[t.Any] = []

            def process_generator(generators: list, index: int = 0) -> None:
                if index >= len(generators):
                    # Base case: all generators processed, evaluate element
                    value = self.visit(node.elt)
                    result.append(value)
                    return

                generator = generators[index]
                iter_obj = self.visit(generator.iter)

                # Save the current environment before processing this generator
                current_env = self.local_env.copy()

                for item in iter_obj:
                    if self._process_generator_item(
                        generator, item, current_env, outer_env
                    ):
                        # Process next generator or append result
                        process_generator(generators, index + 1)

            # Start processing generators recursively
            process_generator(node.generators)
            return result_type(result)
        finally:
            # Restore the outer environment and pop the scope
            self.local_env = outer_env
            self.scope_stack.pop()

    def visit_ListComp(self, node: ast.ListComp) -> list:
        return self._handle_comprehension(node, list)

    def visit_SetComp(self, node: ast.SetComp) -> set:
        return self._handle_comprehension(node, set)

    def visit_DictComp(self, node: ast.DictComp) -> dict[t.Any, t.Any]:
        """Handle dictionary comprehensions."""
        _, outer_env = self._setup_comprehension_scope()

        try:
            result: dict[t.Any, t.Any] = {}

            def process_generator(generators: list, index: int = 0) -> None:
                if index >= len(generators):
                    # Base case: all generators processed, evaluate key-value
                    # pair
                    key = self.visit(node.key)
                    value = self.visit(node.value)
                    result[key] = value
                    return

                generator = generators[index]
                iter_obj = self.visit(generator.iter)

                # Save the current environment before processing this generator
                current_env = self.local_env.copy()

                for item in iter_obj:
                    if self._process_generator_item(
                        generator, item, current_env, outer_env
                    ):
                        # Process next generator or evaluate key-value pair
                        process_generator(generators, index + 1)

            # Start processing generators recursively
            process_generator(node.generators)
            return result
        finally:
            # Restore the outer environment and pop the scope
            self.local_env = outer_env
            self.scope_stack.pop()

    def visit_JoinedStr(self, node: ast.JoinedStr) -> str:
        parts = []
        for value in node.values:
            if isinstance(value, ast.Constant):
                parts.append(str(value.value))
            elif isinstance(value, ast.FormattedValue):
                parts.append(self._format_value(value))
            else:
                raise NotImplementedError(
                    f"Unsupported node type in f-string: {type(value).__name__}"
                )
        return "".join(parts)

    def _format_value(self, node: ast.FormattedValue) -> str:
        """Format a single value in an f-string.

        Args:
            node: FormattedValue AST node

        Returns:
            Formatted string representation of the value

        Raises:
            NotImplementedError: If unsupported conversion or format_spec is
            used
        """
        # Evaluate the expression
        value = self.visit(node.value)

        # Handle conversion specifier (s, r, a)
        if node.conversion == -1:  # No conversion
            converted = value
        elif node.conversion == 115:  # 's' for str()
            converted = str(value)
        elif node.conversion == 114:  # 'r' for repr()
            converted = repr(value)
        elif node.conversion == 97:  # 'a' for ascii()
            converted = ascii(value)
        else:
            raise NotImplementedError(
                f"Unsupported conversion type in f-string: {node.conversion}"
            )

        # Handle format specification
        if node.format_spec is None:
            format_spec = ""
        else:
            # Format spec can itself be an f-string
            format_spec = self.visit(node.format_spec)

        try:
            # Apply the format specification
            if format_spec:
                result = format(converted, format_spec)
            else:
                result = format(converted)
            return result
        except ValueError as e:
            raise ValueError(
                f"Invalid format specification '{format_spec}' "
                f"for value {repr(value)} of type {type(value).__name__}"
            ) from e

    def _check_attribute_security(self, attr_name: str) -> None:
        """Check if attribute access is allowed.

        Args:
            attr_name: Name of the attribute to check

        Raises:
            SecurityError: If attribute access is not allowed
        """
        if attr_name in self.FORBIDDEN_ATTRS:
            raise SecurityError(
                f"Access to '{attr_name}' attribute is not allowed"
            )

    def _get_attribute_safely(self, value: t.Any, attr_name: str) -> t.Any:
        """Get attribute value with proper error handling.

        Args:
            value: Object to get attribute from
            attr_name: Name of the attribute to get

        Returns:
            The attribute value

        Raises:
            AttributeError: If attribute doesn't exist
        """
        try:
            return getattr(value, attr_name)
        except AttributeError as e:
            if isinstance(value, type):
                raise AttributeError(
                    f"type object '{value.__name__}' has no attribute "
                    f"'{attr_name}'"
                ) from e
            else:
                raise AttributeError(
                    f"'{type(value).__name__}' object has no attribute "
                    f"'{attr_name}'"
                ) from e

    def _create_bound_method(
        self, func: t.Any, instance: t.Any, attr_name: str
    ) -> t.Callable[..., t.Any]:
        """Create a bound method for a function.

        Args:
            func: Function to bind
            instance: Instance to bind to
            attr_name: Name of the attribute

        Returns:
            The bound method
        """

        def bound_method(*args, **kwargs):
            prev_env = self.local_env

            try:
                # Check if this is a static method - either by flag or by type
                has_static_flag = getattr(
                    type(instance), f"__static_{attr_name}", False
                )
                is_static_method = isinstance(func, staticmethod)

                # Check if the method is a function
                is_function = isinstance(func, types.FunctionType)

                if has_static_flag or is_static_method:
                    # For static methods, don't bind to instance
                    self.local_env = prev_env
                    if is_static_method:
                        method = func.__get__(None, type(instance))
                        return method(*args, **kwargs)
                    return func(*args, **kwargs)
                elif isinstance(func, classmethod):
                    self.local_env = prev_env
                    method = func.__get__(type(instance), type(instance))
                    return method(*args, **kwargs)
                elif is_function:
                    # If it's a function, call it directly
                    self.local_env = prev_env
                    return func(*args, **kwargs)
                else:
                    self.local_env = prev_env
                    method = func.__get__(instance, type(instance))
                    return method(*args, **kwargs)
            finally:
                self.local_env = prev_env

        return bound_method

    def _create_decorated_method(
        self, func: t.Any, instance: t.Any, decorator_type: type
    ) -> t.Callable[..., t.Any]:
        """Create a method for a decorated function.

        Args:
            func: Function to decorate
            instance: Instance to bind to
            decorator_type: Type of the decorator

        Returns:
            The decorated method
        """
        if isinstance(decorator_type, (classmethod, property)):

            def decorated_method(*args, **kwargs):
                prev_env = self.local_env
                self.local_env = {**prev_env, "self": instance}
                try:
                    return func(*args, **kwargs)
                finally:
                    self.local_env = prev_env

            return decorated_method
        else:
            # For staticmethod, just return the function as is
            return func

    def _should_bind_function(
        self, func: t.Any, instance: t.Any, attr_name: str
    ) -> bool:
        """Check if a function should be bound to an instance.

        Args:
            func: Function to check
            instance: Instance to potentially bind to
            attr_name: Name of the attribute

        Returns:
            Whether the function should be bound
        """
        # Check if this is a registered function
        if registry.is_registered(func):
            return False

        # Check if this is a static method
        if isinstance(instance, type):
            # If accessed on class, check for static marker
            if getattr(instance, f"__static_{attr_name}", False):
                return False
        else:
            # If accessed on instance, check the class
            if getattr(type(instance), f"__static_{attr_name}", False):
                return False

        # If not a static method, check if it's a module function
        if isinstance(instance, types.ModuleType):
            # For module functions, don't bind self
            return False

        # Check if the function is in the global environment
        for global_value in self.global_env.values():
            if isinstance(global_value, dict):
                # Check nested dictionaries
                for nested_value in global_value.values():
                    if func is nested_value:
                        return False
            elif func is global_value:
                return False

        return True

    def visit_Attribute(self, node: ast.Attribute) -> t.Any:
        """Visit an attribute access node.

        Args:
            node: The Attribute AST node

        Returns:
            The value of the attribute

        Raises:
            SecurityError: If accessing a forbidden attribute
            AttributeError: If the attribute doesn't exist
        """
        # Security check
        self._check_attribute_security(node.attr)

        # Get the base value
        value = self.visit(node.value)

        # Get the attribute safely
        attr = self._get_attribute_safely(value, node.attr)

        # Handle function binding
        if isinstance(attr, types.FunctionType):
            if self._should_bind_function(attr, value, node.attr):
                return self._create_bound_method(attr, value, node.attr)
            return attr
        elif isinstance(attr, (classmethod, staticmethod, property)):
            # For decorated methods, get the underlying function
            func = attr.__get__(value, type(value))
            return self._create_decorated_method(func, value, type(attr))

        return attr

    def visit_Subscript(self, node: ast.Subscript) -> t.Any:
        """Handle subscript operations with improved slice support.

        Args:
            node: Subscript AST node

        Returns:
            Value from the subscript operation

        Raises:
            TypeError: If subscript operation is invalid
            IndexError: If index is out of range
        """
        value = self.visit(node.value)

        # Handle different slice types
        if isinstance(node.slice, ast.Index):
            # For Python < 3.9 compatibility
            slice_val = self.visit(node.slice)
            return value[slice_val]
        elif isinstance(node.slice, ast.Slice):
            # Handle slice with start:stop:step syntax
            start = (
                self.visit(node.slice.lower)
                if node.slice.lower is not None
                else None
            )
            stop = (
                self.visit(node.slice.upper)
                if node.slice.upper is not None
                else None
            )
            step = (
                self.visit(node.slice.step)
                if node.slice.step is not None
                else None
            )
            return value[start:stop:step]
        elif (
            isinstance(node.slice, ast.Constant)
            and node.slice.value is Ellipsis
        ):
            # Handle ellipsis subscript (lst[...]) by returning the entire list
            if isinstance(value, list):
                return value[:]
            else:
                raise TypeError(
                    f"'{type(value).__name__}' object does not support "
                    "ellipsis indexing"
                )
        else:
            # For Python >= 3.9, node.slice can be other expression nodes
            slice_val = self.visit(node.slice)
            try:
                return value[slice_val]
            except TypeError as e:
                if isinstance(value, list):
                    raise TypeError(
                        "list indices must be integers or slices, not "
                        f"{type(slice_val).__name__}"
                    ) from e
                elif isinstance(value, dict):
                    raise TypeError(
                        "unhashable type: " f"{type(slice_val).__name__}"
                    ) from e
                else:
                    raise TypeError(
                        f"{type(value).__name__} indices must be integers"
                    ) from e

    def visit_Expr(self, node: ast.Expr) -> t.Any:
        """Visit an expression statement.

        Args:
            node: The Expr AST node

        Returns:
            The value of the expression
        """
        return self.visit(node.value)

    def visit_Expression(self, node: ast.Expression) -> t.Any:
        result = self.visit(node.body)
        self.global_env["_"] = result
        return result

    def visit_Module(self, node: ast.Module) -> t.Any:
        result = None
        for stmt in node.body:
            if isinstance(stmt, ast.Expr):
                # For expression statements, capture the value
                result = self.visit(stmt.value)
                self.global_env["_"] = result
            else:
                # For other statements, just execute them
                self.visit(stmt)
        return result

    def _create_custom_super(
        self,
        class_obj: type | None,
    ) -> t.Callable[..., t.Any]:
        """Create a custom super implementation for a class."""

        def custom_super(cls=None, obj_or_type=None):
            if cls is None and obj_or_type is None:
                # Handle zero-argument super() by finding the calling class
                # and instance from the current scope
                if "self" in self.local_env:
                    obj_or_type = self.local_env["self"]
                    cls = class_obj
                else:
                    raise RuntimeError(
                        "super(): no arguments and no context - unable to "
                        "determine class and instance"
                    )
            elif cls is None:
                # Handle one-argument super()
                if obj_or_type is None:
                    raise TypeError("super() argument 1 cannot be None")
                cls = type(obj_or_type)

            if obj_or_type is None:
                raise TypeError("super() argument 2 cannot be None")

            # Find the next class in the MRO after cls
            mro = (
                obj_or_type.__class__.__mro__
                if isinstance(obj_or_type, object)
                else obj_or_type.__mro__
            )
            for i, base in enumerate(mro):
                if base is cls:
                    if i + 1 < len(mro):
                        next_class = mro[i + 1]

                        def bound_super_method(name, current_class=next_class):
                            method = getattr(current_class, name)
                            if isinstance(method, (staticmethod, classmethod)):
                                return method.__get__(
                                    obj_or_type, current_class
                                )
                            else:
                                return method.__get__(
                                    obj_or_type, current_class
                                )

                        # Create a new class with a __getattr__ method that
                        # will bind self to the method
                        params = {
                            "__getattr__": (
                                lambda _, name, method=bound_super_method: (
                                    method(name)
                                )
                            )
                        }
                        return type("Super", (), params)()
                    break
            raise RuntimeError("super(): bad __mro__")

        return custom_super

    def _process_class_function(
        self, stmt: ast.FunctionDef, namespace: dict[str, t.Any]
    ) -> None:
        """Process a function definition within a class.

        Args:
            stmt: FunctionDef AST node
            namespace: Class namespace dictionary
        """
        # Handle function definition
        self.visit(stmt)

        # Get the function from namespace
        func = namespace[stmt.name]

        # Handle decorators in reverse order
        for decorator in reversed(stmt.decorator_list):
            # Evaluate the decorator
            decorator_func = self.visit(decorator)
            # Apply the decorator
            func = decorator_func(func)

            # For static methods, we need to store both the decorator and the
            # function
            if decorator_func is staticmethod:
                namespace[f"__static_{stmt.name}"] = True

        # Update the function in namespace
        namespace[stmt.name] = func

    def _create_class_namespace(self, node: ast.ClassDef) -> dict[str, t.Any]:
        """Create and populate the class namespace.

        Args:
            node: ClassDef AST node

        Returns:
            The populated class namespace
        """
        namespace: dict[str, t.Any] = {}

        # Save current environment
        prev_env = self.local_env
        self.local_env = namespace

        try:
            # Execute the class body
            for stmt in node.body:
                if isinstance(stmt, ast.FunctionDef):
                    self._process_class_function(stmt, namespace)
                else:
                    self.visit(stmt)
        finally:
            # Restore the environment
            self.local_env = prev_env

        return namespace

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        """Handle class definition with support for inheritance and class body.

        Args:
            node: The ClassDef AST node
        """
        # Create a new scope for the class definition
        with ScopeContext(self):
            # Evaluate base classes
            bases = tuple(self.visit(base) for base in node.bases)

            # Create and populate the class namespace
            namespace = self._create_class_namespace(node)

            # Add custom super to the class namespace (will be updated after
            # class creation)
            namespace["super"] = self._create_custom_super(class_obj=None)

            # Set the module name for the class
            namespace["__module__"] = "monic.expressions.__namespace__"

            # Create the class object
            class_obj = types.new_class(
                node.name, bases, {}, lambda ns: ns.update(namespace)
            )

            # Update super with the actual class object (after class creation)
            namespace["super"] = self._create_custom_super(class_obj=class_obj)

            # Register the class in the current scope
            self._set_name_value(node.name, class_obj)

    def _match_value_pattern(
        self,
        pattern: ast.MatchValue,
        value: t.Any,
    ) -> bool:
        """Match a literal value pattern.

        Args:
            pattern: MatchValue AST node
            value: Value to match against

        Returns:
            Whether the pattern matches the value
        """
        pattern_value = self.visit(pattern.value)
        return type(value) is type(pattern_value) and value == pattern_value

    def _match_sequence_pattern(
        self,
        pattern: ast.MatchSequence,
        value: t.Any,
    ) -> bool:
        """Match a sequence pattern.

        Args:
            pattern: MatchSequence AST node
            value: Value to match against

        Returns:
            Whether the pattern matches the value
        """
        if not isinstance(value, (list, tuple)):
            return False

        # Find star pattern index if exists
        star_idx = -1
        for i, p in enumerate(pattern.patterns):
            if isinstance(p, ast.MatchStar):
                star_idx = i
                break

        if star_idx == -1:
            return self._match_fixed_sequence(pattern.patterns, value)
        else:
            return self._match_star_sequence(pattern.patterns, value, star_idx)

    def _match_fixed_sequence(
        self,
        patterns: list[ast.pattern],
        value: t.Any,
    ) -> bool:
        """Match a sequence pattern without star expressions.

        Args:
            patterns: List of pattern AST nodes
            value: Value to match against

        Returns:
            Whether the pattern matches the value
        """
        if len(patterns) != len(value):
            return False
        return all(self._match_pattern(p, v) for p, v in zip(patterns, value))

    def _match_star_sequence(
        self,
        patterns: list[ast.pattern],
        value: t.Any,
        star_idx: int,
    ) -> bool:
        """Match a sequence pattern with a star expression.

        Args:
            patterns: List of pattern AST nodes
            value: Value to match against
            star_idx: Index of the star pattern

        Returns:
            Whether the pattern matches the value
        """
        if len(value) < len(patterns) - 1:
            return False

        # Match patterns before star
        for p, v in zip(patterns[:star_idx], value[:star_idx]):
            if not self._match_pattern(p, v):
                return False

        # Calculate remaining elements after star
        remaining_count = len(patterns) - star_idx - 1

        # Match patterns after star
        for p, v in zip(
            patterns[star_idx + 1 :],
            value[-remaining_count:] if remaining_count > 0 else [],
        ):
            if not self._match_pattern(p, v):
                return False

        # Bind star pattern if it has a name
        star_pattern = patterns[star_idx]
        if isinstance(star_pattern, ast.MatchStar) and star_pattern.name:
            star_value = (
                list(value[star_idx:-remaining_count])
                if remaining_count > 0
                else list(value[star_idx:])
            )
            self._set_name_value(star_pattern.name, star_value)
            self.current_scope.locals.add(star_pattern.name)

        return True

    def _match_mapping_pattern(
        self,
        pattern: ast.MatchMapping,
        value: t.Any,
    ) -> bool:
        """Match a mapping pattern.

        Args:
            pattern: MatchMapping AST node
            value: Value to match against

        Returns:
            Whether the pattern matches the value
        """
        if not isinstance(value, dict):
            return False

        # Check if all required keys are present
        for key in pattern.keys:
            key_value = self.visit(key)
            if key_value not in value:
                return False

        # Match each key-pattern pair
        for key, pat in zip(pattern.keys, pattern.patterns):
            key_value = self.visit(key)
            if not self._match_pattern(pat, value[key_value]):
                return False

        # Handle rest pattern if present
        if pattern.rest is not None:
            rest_dict = {
                k: v
                for k, v in value.items()
                if not any(self.visit(key) == k for key in pattern.keys)
            }
            self._set_name_value(pattern.rest, rest_dict)
            self.current_scope.locals.add(pattern.rest)

        return True

    def _match_or_pattern(
        self,
        pattern: ast.MatchOr,
        value: t.Any,
    ) -> bool:
        """Match an OR pattern.

        Args:
            pattern: MatchOr AST node
            value: Value to match against

        Returns:
            Whether the pattern matches the value
        """
        for p in pattern.patterns:
            # Create a temporary scope for each OR pattern
            # to avoid variable binding conflicts
            temp_scope = Scope()
            self.scope_stack.append(temp_scope)
            try:
                if self._match_pattern(p, value):
                    return True
            finally:
                self.scope_stack.pop()
        return False

    def _match_class_pattern(
        self,
        pattern: ast.MatchClass,
        value: t.Any,
    ) -> bool:
        """Match a class pattern.

        Args:
            pattern: MatchClass AST node
            value: Value to match against

        Returns:
            Whether the pattern matches the value
        """
        cls = self.visit(pattern.cls)
        if not isinstance(value, cls):
            return False

        # Get positional attributes from __match_args__
        match_args = getattr(cls, "__match_args__", ())
        if len(pattern.patterns) > len(match_args):
            return False

        # Match positional patterns
        for pat, attr_name in zip(pattern.patterns, match_args):
            if not self._match_pattern(pat, getattr(value, attr_name)):
                return False

        # Match keyword patterns
        for name, pat in zip(pattern.kwd_attrs, pattern.kwd_patterns):
            if not hasattr(value, name):
                return False
            if not self._match_pattern(pat, getattr(value, name)):
                return False

        return True

    def _match_as_pattern(
        self,
        pattern: ast.MatchAs,
        value: t.Any,
    ) -> bool:
        """Match an AS pattern.

        Args:
            pattern: MatchAs AST node
            value: Value to match against

        Returns:
            Whether the pattern matches the value
        """
        if pattern.pattern is not None:
            if not self._match_pattern(pattern.pattern, value):
                return False
        if pattern.name is not None:
            self._set_name_value(pattern.name, value)
            self.current_scope.locals.add(pattern.name)
        return True

    def _match_star_pattern(
        self,
        pattern: ast.MatchStar,
        value: t.Any,
    ) -> bool:
        """Match a star pattern.

        Args:
            pattern: MatchStar AST node
            value: Value to match against

        Returns:
            Whether the pattern matches the value
        """
        if pattern.name is not None:
            self._set_name_value(pattern.name, value)
            self.current_scope.locals.add(pattern.name)
        return True

    def _match_pattern(
        self,
        pattern: ast.pattern,
        value: t.Any,
    ) -> bool:
        """Match a pattern against a value.

        Args:
            pattern: Pattern AST node
            value: Value to match against

        Returns:
            Whether the pattern matches the value
        """
        if isinstance(pattern, ast.MatchValue):
            return self._match_value_pattern(pattern, value)
        elif isinstance(pattern, ast.MatchSingleton):
            return value is pattern.value
        elif isinstance(pattern, ast.MatchSequence):
            return self._match_sequence_pattern(pattern, value)
        elif isinstance(pattern, ast.MatchMapping):
            return self._match_mapping_pattern(pattern, value)
        elif isinstance(pattern, ast.MatchStar):
            return self._match_star_pattern(pattern, value)
        elif isinstance(pattern, ast.MatchAs):
            return self._match_as_pattern(pattern, value)
        elif isinstance(pattern, ast.MatchOr):
            return self._match_or_pattern(pattern, value)
        elif isinstance(pattern, ast.MatchClass):
            return self._match_class_pattern(pattern, value)

        return False

    def visit_Match(self, node: ast.Match) -> None:
        """Handle match-case statements.

        Args:
            node: Match AST node

        Example:
            match value:
                case 1:
                    ...
                case [x, y]:
                    ...
                case {"key": value}:
                    ...
                case _:
                    ...
        """
        # Evaluate the subject expression
        subject = self.visit(node.subject)

        # Create a new scope for pattern matching
        with ScopeContext(self):
            # Try each case in order
            for case in node.cases:
                pattern = case.pattern

                # Create a temporary scope for pattern matching
                with ScopeContext(self):
                    # Try to match the pattern
                    if not self._match_pattern(pattern, subject):
                        # If no match, continue to the next case
                        continue

                    # If there's a guard, evaluate it
                    if case.guard is not None:
                        # Evaluate the guard expression
                        guard_result = self.visit(case.guard)
                        if not guard_result:
                            # If the guard fails, continue to the next case
                            continue

                    # Copy matched variables from temp scope to match scope
                    for name in self.current_scope.locals:
                        if name in self.local_env:
                            self._set_name_value(name, self.local_env[name])

                    # Execute the case body
                    for stmt in case.body:
                        self.visit(stmt)

                    # Return the match statement since we found a match
                    return
