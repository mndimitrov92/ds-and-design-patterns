"""
Factory Method, Factory and Abstract Factory design patterns
INTENT:
    Factory Method is a creational design pattern that provides an interface for creating objects in a superclass,
    but allows subclasses to alter the type of objects that will be created.

    Abstract Factory is a creational design pattern that lets you produce families of related
    objects without specifying their concrete classes.
APPLICABILITY:
    *Use the Factory Method when you don’t know beforehand the exact types and dependencies of the objects your code should work with.
        The Factory Method separates product construction code from the code that actually uses the product.
        Therefore it’s easier to extend the product construction code independently from the rest of the code.
    *Use the Factory Method when you want to provide users of your library or framework with a way to extend its internal components.
    *Use the Factory Method when you want to save system resources by reusing existing objects instead of rebuilding them each time.

    ^ Use the Abstract Factory when your code needs to work with various families of related products, but you
    don’t want it to depend on the concrete classes of those products—they might be unknown beforehand or you
    simply want to allow for future extensibility.

PROS AND CONS:
    Factory method:
        PROS:
            *You avoid tight coupling between the creator and the concrete products.
            *Single Responsibility Principle. You can move the product creation code into one place in the program,
                making the code easier to support.
            *Open/Closed Principle. You can introduce new types of products into the program without breaking existing client code.
        CONS:
            *The code may become more complicated since you need to introduce a lot of new subclasses to implement
            the pattern. The best case scenario is when you’re introducing the pattern into an existing hierarchy of creator classes.
    Abstract Factory:
        PROS:
            *You can be sure that the products you’re getting from a factory are compatible with each other.
            *You avoid tight coupling between concrete products and client code.
            *Single Responsibility Principle. You can extract the product creation code into one place, making the code easier to support.
            *Open/Closed Principle. You can introduce new variants of products without breaking existing client code.
        CONS:
            *The code may become more complicated than it should be, since a lot of new interfaces and classes are
            introduced along with the pattern.
USAGE:
    Factory Method:
        The Factory Method pattern is widely used in Python code. It’s very useful when you need to provide a high level
        of flexibility for your code.
    Abstract Factory:
        The Abstract Factory pattern is pretty common in Python code. Many frameworks and libraries use it to provide a
        way to extend and customize their standard components.
IDENTIFICATION:
    Factory method:
        Factory methods can be recognized by creation methods, which create objects from concrete classes,
        but return them as objects of abstract type or interface.
    Abstract Factory:
        The pattern is easy to recognize by methods, which return a factory object.
        Then, the factory is used for creating specific sub-components.
"""
from math import sin, cos
from abc import ABC


################### Factory method ##############
# Any method that returns an object
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x} and y: {self.y}"

    # Factory methods
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


def test_factory_method():
    p1 = Point.new_cartesian_point(2, 3)
    p2 = Point.new_polar_point(1, 2)
    print(p1)
    print(p2)


#################### Factory #####################
# The idea is that once you have two many factory methods in a class to move them in a Factory class
# From the above example, the changes needed to make it a Factory are:
class Pointv2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x} and y: {self.y}"

    # It can be outside the class or inside(like so)
    class PointFactory:
        @staticmethod
        def new_cartesian_point(x, y):
            return Pointv2(x, y)

        @staticmethod
        def new_polar_point(rho, theta):
            return Pointv2(rho * cos(theta), rho * sin(theta))

        # The methods can be non-static as well if they need to access some instance specific values
        def new_cartesian_point_nonstatic(self, x, y):
            # Accessing this method will be p= Point.PointFactory.new_cartesian_point_nonstatic(2,3)
            p = Point()
            p.x = 2
            p.y = 3
            return p


############### Abstract Factory ################
# Idea is that if there are a hierarchy of types, then you can have a corresponding hierarchy of factories
class HotDrink(ABC):
    """Base class"""

    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("I'm drinking tea.")


class Coffee(HotDrink):
    def consume(self):
        print("I'm drinking coffee.")


class BaseFactory(ABC):
    def prepare(self):
        pass


class TeaFactory(BaseFactory):
    def prepare(self):
        # Here you can manipulate parameters and so on
        print("I'm preparing tea")
        return Tea()


class CoffeeFactory(BaseFactory):
    def prepare(self):
        print("Preparing coffee")
        return Coffee()


def make_drink(entry):
    # With this approach the open-closed principle is being broken
    if entry == "tea":
        drink = TeaFactory().prepare()
    elif entry == "coffee":
        drink = CoffeeFactory().prepare()
    else:
        drink = None
    return drink


def test_abstract_factory():
    entry = input("What kind of drink do you want")
    drink = make_drink(entry)
    drink.consume()


if __name__ == '__main__':
    print("Factory method:")
    test_factory_method()

    print("Abstract Factory:")
    test_abstract_factory()
