"""
Adapter design pattern

INTENT:
    Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate.
APPLICABILITY:
    *Use the Adapter class when you want to use some existing class, but its interface isn’t compatible with the rest of your code.
    *Use the pattern when you want to reuse several existing subclasses that lack some common functionality that can’t be added to the superclass.
PROS AND CONS:
    PROS:
        *Single Responsibility Principle. You can separate the interface or data conversion code from the primary business logic of the program.
        *Open/Closed Principle. You can introduce new types of adapters into the program without breaking the existing
         client code, as long as they work with the adapters through the client interface.
    CONS:
        *The overall complexity of the code increases because you need to introduce a set of new interfaces and classes.
         Sometimes it’s simpler just to change the service class so that it matches the rest of your code
USAGE:
    The Adapter pattern is pretty common in Python code. It’s very often used in systems based on some legacy code.
    In such cases, Adapters make legacy code with modern classes.
IDENTIFICATION:
    Adapter is recognizable by a constructor which takes an instance of different abstract/interface type.
    When adapter receives a call to any of its methods, it translates parameters to appropriate format and then directs
    the call to one or several methods of the wrapped object.
"""


# Client code that needs to be adapted
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_point(p):
    print(".", end="")


# The adapter
class LineToPointAdapter(list):
    count = 0

    def __init__(self, line):
        print(f"{self.count}: Generating points for line"
              f"[{line.start.x}, {line.start.y}] ->"
              f"[{line.end.x}, {line.end.y}]")

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = max(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)

        if right - left == 0:
            for y in range(top, bottom):
                self.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                self.append(Point(x, top))


def draw(rectangles):
    print("---Drawing some stuff---")
    for rect in rectangles:
        for line in rect:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)


# The Adaptee that need to work with the client code
class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Rectangle(list):
    """Represented as a list of lines"""

    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


def test_adapter():
    recs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(2, 2, 6, 6)
    ]
    draw(recs)
    # Drawback with this approach is that if the draw function is called again, the same points will be drawn again
    # in this case caching the already drawn points is the solution


### A simpler illustration of an adapter
# We have a class Square
class Square:
    def __init__(self, side=0):
        self.side = side


# And this method that takes a rectangle and calculates the area
def calc_area(rect):
    return rect.width * rect.height


# In order for the calc area to work we need to create an adapter that exposes width and height properties of the
# rect object
class RectAdapter:
    def __init__(self, square):
        self.square = square

    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side


if __name__ == '__main__':
    print("Adapter test:")
    test_adapter()
