"""
Composite design pattern

INTENT:
    Composite is a structural design pattern that lets you compose objects into tree structures and then work with these
    structures as if they were individual objects.
APPLICABILITY:
    *Use the Composite pattern when you have to implement a tree-like object structure.
    *Use the pattern when you want the client code to treat both simple and complex elements uniformly.
PROS AND CONS:
    PROS:
        *You can work with complex tree structures more conveniently: use polymorphism and recursion to your advantage.
        *Open/Closed Principle. You can introduce new element types into the app without breaking the existing code,
         which now works with the object tree.
    CONS:
        *It might be difficult to provide a common interface for classes whose functionality differs too much.
         In certain scenarios, you’d need to overgeneralize the component interface, making it harder to comprehend.
    USAGE:
        The Composite pattern is pretty common in Python code. It’s often used to represent hierarchies of
        user interface components or the code that works with graphs.
    IDENTIFICATION:
        If you have an object tree, and each object of a tree is a part of the same class hierarchy, this is
        most likely a composite. If methods of these classes delegate the work to child objects of the tree and do it
        via the base class/interface of the hierarchy, this is definitely a composite.

"""


# Composite example
class GraphicObject:
    def __init__(self, color=None):
        self.color = color
        self.children = []
        self._name = "Group"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def _print(self, items, depth):
        items.append("*" * depth)
        if self.color:
            items.append(f"{self.color}")
        items.append(f"{self.name}\n")
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self):
        items = []
        self._print(items, 0)
        return "".join(items)


class Circle(GraphicObject):
    @property
    def name(self):
        return "Circle"


class Square(GraphicObject):
    @property
    def name(self):
        return "Square"


def test_composite():
    drawing = GraphicObject()
    drawing.name = "My Picture"

    drawing.children.append(Circle("Blue"))
    drawing.children.append(Square("Red"))
    # Create a subgroup
    group = GraphicObject()
    group.children.append(Circle("Yellow"))
    group.children.append(Square("Yellow"))
    # Add the subgroup to the main group
    drawing.children.append(group)
    print(drawing)


if __name__ == '__main__':
    print("Test composite:")
    test_composite()
