"""
Decorator design pattern
INTENT:
    Decorator is a structural design pattern that lets you attach new behaviors to objects by placing these objects
    inside special wrapper objects that contain the behaviors.
APPLICABILITY:
    *Use the Decorator pattern when you need to be able to assign extra behaviors to objects at runtime
     without breaking the code that uses these objects.
    *Use the pattern when it’s awkward or not possible to extend an object’s behavior using inheritance.
PROS AND CONS:
    PROS:
        *You can extend an object’s behavior without making a new subclass.
        *You can add or remove responsibilities from an object at runtime.
        *You can combine several behaviors by wrapping an object into multiple decorators.
        *Single Responsibility Principle. You can divide a monolithic class that implements many possible variants of
         behavior into several smaller classes.
    CONS:
        *It’s hard to remove a specific wrapper from the wrappers stack.
        *It’s hard to implement a decorator in such a way that its behavior doesn’t depend on the order in the decorators stack.
        *The initial configuration code of layers might look pretty ugly.
USAGE:
    The Decorator is pretty standard in Python code, especially in code related to streams.
IDENTIFICATION:
    Decorator can be recognized by creation methods or constructor that accept objects of the same class or interface as a current class.
"""
import time
from abc import ABC


# Functional decorator
def time_it_decorator(func):
    """Decorator for timing function execution time"""

    def wrapper():
        start = time.time()
        result = func()
        total = time.time() - start
        print(f"Function: {func.__name__} took {int(total) * 1000}ms")
        return result

    return wrapper


@time_it_decorator
def some_func():
    print("Starting some process")
    time.sleep(1)
    print("Done")
    return 1


########### Classic decorator (class that augments the functionality of an existing class)
class Shape(ABC):
    """Base class for the shape"""

    def __str__(self):
        return ""


# Adding color decorator for the shape
class ColoredShape(Shape):
    # One of the parameters are the decorated(shape) object that will be decorated
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def __str__(self):
        return f"{self.shape} has the color {self.color}"


# Transparency decorator
class TransparentShape(Shape):
    # One of the parameters are the decorated(shape) object that will be decorated
    def __init__(self, shape, transparency):
        # There is however nothing stop for adding a decorator multiple times
        # to prevent this, check it the object is already a decorated instance
        if isinstance(shape, TransparentShape):
            raise Exception("Cannot apply the same decorator twice")
        self.shape = shape
        self.transparency = transparency

    def __str__(self):
        return f"{self.shape} has a transparency of {self.transparency}"


# Different shape objects
class Circle(Shape):
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"Circle of size {self.size}"

    def resize(self, factor):
        print(f"Resizing to: {self.size * factor}")
        self.size = self.size * factor


def test_classic_decorator():
    # Normal use (without the decorator)
    circle = Circle(2)
    print(circle)
    # Decorating the circle by passing the circle object to the decorator class and adding the new feature
    red_circle = ColoredShape(circle, "red")
    print(red_circle)
    # Another issue is that since decorated object is now a ColorShaped object
    # we cannot access other methods apart from the ones defined in the decorator class
    # which means that we cannot access in this case the resize method of the circle
    # red_circle.resize() will throw an exception

    # decorating the already decorated object
    transparent_red_circle = TransparentShape(red_circle, 0.5)
    print(transparent_red_circle)
    # The decorator can be applied multiple times which may not be desirable
    multidecorated = TransparentShape(TransparentShape(red_circle, 0.2), 0.4)
    print(multidecorated)


# Dynamic decorator , almost the same as the classic decorator, but also provides a way to handle and make
# accessible the methods from the decorated object though the decorator which is a problem with the classic decorator
class ColoredShapeDynamic(Shape):
    # One of the parameters are the decorated(shape) object that will be decorated
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def __str__(self):
        return f"{self.shape} has the color {self.color}"

    # To access the methods of the shape object we need to redefine the gettattr, setattr and delattr methods
    # whichever is needed
    def __getattr__(self, item):
        return getattr(self.__dict__["shape"], item)

    def __setattr__(self, key, value):
        if key == "shape":
            self.__dict__[key] = value
        else:
            setattr(self.__dict__["shape"], key, value)

    def __delattr__(self, item):
        delattr(self.__dict__["shape"], item)

    # A way to call a method which was defined only for some of the decorated objects
    # in this case resize is only available in the Circle class
    def resize_circle(self, factor):
        # Check if the shape object has e resize attribute, if not, return None as default
        result = getattr(self.shape, "resize,", None)
        # Try it attribute is callable and assign the new value
        if callable(result):
            self.shape.resize(factor)

def test_dynamic_decorator():
    # Undecorated
    circle = Circle(4)
    print(circle)

    # Decorated
    dynamic_decorated_circle = ColoredShapeDynamic(circle, "blue")
    print(dynamic_decorated_circle)
    # Calling the resize method of the circle object is now available
    print(dynamic_decorated_circle.resize(2))
    print(dynamic_decorated_circle)


if __name__ == '__main__':
    print("Functional decorator:")
    # One way of using calling the decorated function
    # time_it_decorator(some_func)()
    # Usual way is to decorate the function
    # some_func()

    print("Classic decorator:")
    # test_classic_decorator()

    print("Dynamic decorator:")
    test_dynamic_decorator()
