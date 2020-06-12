"""
Chain of responsibility design pattern

INTENT:
    Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain of handlers.
    Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.
APPLICABILITY:
    *Use the Chain of Responsibility pattern when your program is expected to process different kinds of requests
     in various ways, but the exact types of requests and their sequences are unknown beforehand.
    *Use the pattern when it’s essential to execute several handlers in a particular order.
    *Use the CoR pattern when the set of handlers and their order are supposed to change at runtime.
PROS AND CONS:
    PROS:
        *You can control the order of request handling.
        *Single Responsibility Principle. You can decouple classes that invoke operations from classes that perform operations.
        *Open/Closed Principle. You can introduce new handlers into the app without breaking the existing client code.
    CONS:
        *Some requests may end up unhandled.
USAGE:
    The Chain of Responsibility pattern isn’t a frequent guest in a Python program since it’s only relevant when code
     operates with chains of objects.
IDENTIFICATION:
    The pattern is recognizable by behavioral methods of one group of objects indirectly call the same methods in
    other objects, while all the objects follow the common interface.
"""


# Method chain of responsibility
class Creature:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defence = defense

    def __str__(self):
        return f"{self.name}  ({self.attack} / {self.defence})"


class CreatureModifier:
    """Base class for the chain of responsibilities"""

    def __init__(self, creature):
        # The object on which the modifiers will be applied
        self.creature = creature
        # Pointer to the next modifier
        self.next_modifier = None

    def add_modifier(self, modifier):
        """Method for adding modifiers to the chain"""
        # If there is a next modifier, apply the add_modifier on it
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            # otherwise store the next modifier
            self.next_modifier = modifier

    def handle(self):
        """This is the location where the modifiers are applied on the creature"""
        # It is up to the inheritors to add value to this method, in the base class it just needs to call
        # the next modifiers handle
        if self.next_modifier:
            self.next_modifier.handle()


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f"Double the {self.creature.name}\'s attack")
        self.creature.attack *= 2
        # Here we have to call the base classes handle method
        # which propagates the chain of responsibility
        super().handle()


class IncreaseDefenceModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack <= 4:
            print(f"Increasing defence by 5")
            self.creature.defence += 5
        super().handle()


# If we want to stop the chain of responsibility
class NoBonusModifier(CreatureModifier):
    def handle(self):
        # By not calling super.handle will stop the chain
        print("No bonuses allowed")


def test_chain_of_responsibility_method():
    goblin = Creature("Goblin", 2, 2)
    print(goblin)
    # Building the modifiers will need to start from the top level element (the modifier root)
    # The baseclass, however, does not do anything but we can apply modifier under the root
    root = CreatureModifier(goblin)
    # If we need to stop after a particular modifier
    # root.add_modifier(NoBonusModifier(goblin))
    # by running the above line, the below modifiers will not be executed
    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(IncreaseDefenceModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.handle()
    print(goblin)


if __name__ == '__main__':
    print("Chain of responsibility method:")
    test_chain_of_responsibility_method()
