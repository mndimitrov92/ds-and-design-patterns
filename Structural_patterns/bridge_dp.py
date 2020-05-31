"""
Bridge design pattern

INTENT:
    Bridge is a structural design pattern that lets you split a large class or a set of closely related classes into two
    separate hierarchies—abstraction and implementation—which can be developed independently of each other.
APPLICABILITY:
    *Use the Bridge pattern when you want to divide and organize a monolithic class that has several variants
    of some functionality (for example, if the class can work with various database servers).
    *Use the pattern when you need to extend a class in several orthogonal (independent) dimensions.
    *Use the Bridge if you need to be able to switch implementations at runtime.
PROS AND CONS:
    PROS:
        *You can create platform-independent classes and apps.
        *The client code works with high-level abstractions. It isn’t exposed to the platform details.
        *Open/Closed Principle. You can introduce new abstractions and implementations independently from each other.
        *Single Responsibility Principle. You can focus on high-level logic in the abstraction and on platform details
         in the implementation.
    CONS:
        *You might make the code more complicated by applying the pattern to a highly cohesive class.
APPLICABILITY:
    The Bridge pattern is especially useful when dealing with cross-platform apps, supporting multiple types of
    database servers or working with several API providers of a certain kind (for example, cloud platforms, social networks, etc.)
IDENTIFICATION:
    Bridge can be recognized by a clear distinction between some controlling entity and several different platforms that it relies on.

Main idea is connecting components through abstractions
Example:
class AbstractClass(ABC):
    In order for the concrete classes to follow a specific implementation flow
    @abstractmethod
    def some_operation(self):
        pass


class ConcreteClass1(AbstractClass):
    def some_operation(self):
        Do some specific stuff

class ConcreteClass2(AbstractClass):
    def some_operation(self):
        Do some specific stuff for this case

class AbstractionClass:
    def __init__(self, concrete_class):
        # Abstraction class is being passed a concrete class object that it handles
        self.concrete_class = concrete_class

The client then uses the abstraction class with the needed concrete implementation
def client_code(abstraction):
    abstraction.some_operation()

first_implementation = ConcreteClass1()
abstraction = AbstractionClass(first_implementation) #In case the client code needs to use the first concrete implementation
client_code(abstraction)
"""
from abc import ABC


# Example bridge implementation for rendering objects with different renderers, this implementation breaks the open-closed
# principle because the renderer is tied to rendering circle, adding new shapes will require addind a new render function
# and then add the corresponding rendering function in both renderers
class Renderer(ABC):
    def render_circle(self):
        pass
    # render_square(self):


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle with radius {radius}")


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing pixels for a circle with radius {radius}")


class Shape:
    """The bridge class"""

    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        pass

    def resize(self, factor):
        pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        # Use the bridge here
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


def test_bridge():
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
    # Same usage but with the raster renderer
    circle2 = Circle(raster, 5)
    circle2.draw()
    circle2.resize(2)
    circle2.draw()


if __name__ == '__main__':
    print("Test the bridge pattern:")
    test_bridge()
