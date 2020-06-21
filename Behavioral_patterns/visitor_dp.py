"""
Visitor design pattern

INTENT:
    Visitor is a behavioral design pattern that lets you separate algorithms from the objects on which they operate.
APPLICABILITY:
    *Use the Visitor when you need to perform an operation on all elements of a complex object structure
     (for example, an object tree).
    * Use the Visitor to clean up the business logic of auxiliary behaviors.
    *Use the pattern when a behavior makes sense only in some classes of a class hierarchy, but not in others.
PROS AND CONS:
    PROS:
        *Open/Closed Principle. You can introduce a new behavior that can work with objects of different classes without
         changing these classes.
        *Single Responsibility Principle. You can move multiple versions of the same behavior into the same class.
        *A visitor object can accumulate some useful information while working with various objects. This might be handy
         when you want to traverse some complex object structure, such as an object tree, and apply the visitor to each object of this structure.
    CONS:
        *You need to update all visitors each time a class gets added to or removed from the element hierarchy.
        *Visitors might lack the necessary access to the private fields and methods of the elements that they’re supposed to work with.
USAGE:
    Visitor isn’t a very common pattern because of its complexity and narrow applicability.
"""


# Intrusive visitor example
class DoubleExpression:
    def __init__(self, value):
        self.value = value

    def print_(self, buffer):
        buffer.append(str(self.value))

    def eval_(self):
        return self.value

    def accept(self, visitor):
        # Method pointing to the appropriate visit method from the visitor class
        visitor.visit(self)


class AdditionExpression:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def print_(self, buffer):
        # In this case the buffer is the object actually visiting both expressions
        buffer.append("(")
        self.left.print_(buffer)
        buffer.append("+")
        self.right.print_(buffer)
        buffer.append(")")

    def eval_(self):
        return self.left.eval_() + self.right.eval_()

    def accept(self, visitor):
        # Method pointing to the appropriate visit method from the visitor class
        visitor.visit(self)


def test_intrusive_visitor():
    # 1 + (2 + 3)
    # These is no classic visitor here, as we modify existing code and break the open-closed principle
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    buffer = []
    e.print_(buffer)
    print("".join(buffer), ' = ', e.eval_())


# Reflective visitor, the advantage here is that all the printing stuff is in a separate class
class ExpressionPrinter:
    @staticmethod
    def print(expression, buffer):
        # the expression and the buffer we want to print
        if isinstance(expression, DoubleExpression):
            buffer.append(str(expression.value))
        elif isinstance(expression, AdditionExpression):
            buffer.append("(")
            ExpressionPrinter.print(expression.left, buffer)
            buffer.append("+")
            ExpressionPrinter.print(expression.right, buffer)
            buffer.append(")")


def test_reflective_visitor():
    # Same example
    # 1 + (2 + 3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    buffer = []
    ExpressionPrinter.print(e, buffer)
    print("".join(buffer))


# Classic visitor, double dispatch
def _qualname(obj):
    """Get the fully-qualified name of an object (including module)."""
    return obj.__module__ + '.' + obj.__qualname__


def _declaring_class(obj):
    """Get the name of the class that declared an object."""
    name = _qualname(obj)
    return name[:name.rfind('.')]


# Stores the actual visitor methods
_methods = {}


# Delegating visitor implementation
def _visitor_impl(self, arg):
    """Actual visitor method implementation."""
    method = _methods[(_qualname(type(self)), type(arg))]
    return method(self, arg)


# The actual @visitor decorator
def visitor(arg_type):
    """Decorator that creates a visitor method."""

    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn

        # Replace all decorated methods with _visitor_impl
        return _visitor_impl

    return decorator


class ClassicExpressionPrinter:
    def __init__(self):
        self.buffer = []

    # decorating the methods would allow double overloading and also specifies which expression
    # should be used for each of the methods
    @visitor(DoubleExpression)
    def visit(self, double_expression):
        self.buffer.append(str(double_expression.value))

    @visitor(AdditionExpression)
    def visit(self, addition_expression):
        # The different representations of the expressions
        self.buffer.append("(")
        addition_expression.left.accept(self)
        self.buffer.append("+")
        addition_expression.right.accept(self)
        self.buffer.append(")")

    def __str__(self):
        return "".join(self.buffer)


def test_classic_visitor():
    # Same example
    # 1 + (2 + 3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    printer = ClassicExpressionPrinter()
    printer.visit(e)
    print(printer)


if __name__ == '__main__':
    print("Intrusive visitor:")
    test_intrusive_visitor()

    print("Reflective visitor:")
    test_reflective_visitor()

    print("Classic visitor:")
    test_classic_visitor()
