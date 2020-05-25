"""
Open - closed principle (open for extension but closed for modification)
New functionality must be added by extension rather than modification
"""
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# Example class that will violate this principle and is not scalable
class FilterClass:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    # If a new filter is needed  later for size like below, violates this principle
    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    # Another additional filter
    def filter_by_size_color(self, products, size, color):
        for p in products:
            if p.size == size and p.color == color:
                yield p


# Another way which follows this principle, in this case we can use
# Enterprise patterns one of which is: Specification
class Specification:
    """Base class which determines whether a particular item satisfy a particular criteria"""

    def is_satisfied(self, item):
        pass

    # Overload the & operator
    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    """Base filter class"""

    def filter(self, items, specification):
        pass


# If you want to filter by color add the color specification and filter classes
#
class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


# Combinator
class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all([x.is_satisfied(item) for x in self.args])


class BetterFilter(Filter):

    def filter(self, items, specification):
        for item in items:
            if specification.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]
    # unoptimal  old way way
    pf = FilterClass()
    print("Filter green products the old way:")
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f" - {p.name} is green.")

    # The approach following the open closed principle
    bf = BetterFilter()
    print("Filter the green products the new way:")
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f" - {p.name} is green.")

    print("Large products:")
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f" - {p.name} is large.")

    # Combined filter for size and color
    print("Large blue items:")
    #large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    # By overloading the & operator the above row can be switched to:
    large_blue = large & ColorSpecification(Color.BLUE)
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large_blue):
        print(f" - {p.name} is large and blue.")
