"""
Strategy design pattern

INTENT:
    Strategy is a behavioral design pattern that lets you define a family of algorithms, put each of them
     into a separate class, and make their objects interchangeable.
APPLICABILITY:
    *Use the Strategy pattern when you want to use different variants of an algorithm within an object and be able to
     switch from one algorithm to another during runtime.
    *Use the Strategy when you have a lot of similar classes that only differ in the way they execute some behavior.
    *Use the pattern to isolate the business logic of a class from the implementation details of algorithms that may
     not be as important in the context of that logic.
    *Use the pattern when your class has a massive conditional operator that switches between different variants of the same algorithm.
PROS AND CONS:
    PROS:
        *You can swap algorithms used inside an object at runtime.
        *You can isolate the implementation details of an algorithm from the code that uses it.
        *You can replace inheritance with composition.
        *Open/Closed Principle. You can introduce new strategies without having to change the context.
    CONS:
        *If you only have a couple of algorithms and they rarely change, there’s no real reason to overcomplicate the
         program with new classes and interfaces that come along with the pattern.
        *Clients must be aware of the differences between strategies to be able to select a proper one.
        *A lot of modern programming languages have functional type support that lets you implement different versions
        of an algorithm inside a set of anonymous functions. Then you could use these functions exactly as you’d have
        used the strategy objects, but without bloating your code with extra classes and interfaces.
USAGE:
    The Strategy pattern is very common in Python code. It’s often used in various frameworks to provide users a way
    to change the behavior of a class without extending it.
IDENTIFICATION:
    Strategy pattern can be recognized by a method that lets nested object do the actual work, as well as the setter
    that allows replacing that object with a different one.
"""
from abc import ABC


class Strategy(ABC):
    """Common base class for the strategies"""

    def start(self, buffer):
        pass

    def end(self, buffer):
        pass

    def add_list_item(self, buffer, item):
        pass


class MarkdownStrategy(Strategy):
    """Visualizing the list items as bullets (first strategy)"""

    def add_list_item(self, buffer, item):
        buffer.append(f"* {item}")


class HTMLStrategy(Strategy):
    """Visualizing the list items as html elements (second strategy)"""

    def start(self, buffer):
        buffer.append("<ul>")

    def end(self, buffer):
        buffer.append("</ul>")

    def add_list_item(self, buffer, item):
        buffer.append(f"    <li>{item}</li>")


class TextProcessor:
    def __init__(self, strategy=MarkdownStrategy()):
        # list containing the items to be visualized
        self.buffer = []
        # Parameter at which the different strategies will be passed
        self.strategy = strategy

    @property
    def get_strategy(self):
        return self.strategy

    @get_strategy.setter
    def set_strategy(self, new_strategy):
        self.strategy = new_strategy

    def append_list(self, items):
        # The different implementation will be handled by the strategy classes
        self.strategy.start(self.buffer)
        for item in items:
            self.strategy.add_list_item(self.buffer, item)
        self.strategy.end(self.buffer)

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return '\n'.join(self.buffer)


def test_strategy():
    items = ["item1", "item2", "item3"]
    tp = TextProcessor()
    tp.append_list(items)
    print(tp)
    # Change the strategy runtime
    tp.clear()
    tp.set_strategy = HTMLStrategy()
    tp.append_list(items)
    print(tp)


if __name__ == '__main__':
    print("Strategy:")
    test_strategy()
