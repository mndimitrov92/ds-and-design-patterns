"""
Liskov substitution principle.
Using a derived class should not break any functionality.
You should be able to substitute a based type with a subtype
"""


# Example of a violation of this principle
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Width: {self.width}, Height: {self.height}"


# The rectangle derived class
class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    # These setters directly violate the principle
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc):
    w = rc.width
    # Change the height of the rectangle
    rc.height = 10
    expected = int(w * 10)
    print(f"Expected area: {expected}, but got {rc.area}")


if __name__ == '__main__':
    rc = Rectangle(2, 3)
    use_it(rc)

    sq = Square(5)
    # The derived class breaks the principle because the behavior of this function is changed
    use_it(sq)
