"""
Dependency inversion principle
High level modules should not depend on low level modules, they should depend on abstraction
Essentially they should depend on interfaces instead of concrete implementation
"""
from enum import Enum
from abc import abstractmethod


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children(self, name):
        pass


class Relationships(RelationshipBrowser):  # Low level module
    def __init__(self):
        self.relations = []

    def add_parent_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    # Handling the relationships should be done here
    def find_all_children(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:  # High-level module
    # def __init__(self, relationships):
    # Depends on the storage implementation
    # if relations is changed to a different storage, the code will break
    # relations = relationships.relations
    # for r in relations:
    #     if r[0].name == "John" and r[1] == Relationship.PARENT:
    #         print(f"John has a child called {r[2].name}")

    def __init__(self, browser):
        for p in browser.find_all_children("John"):
            print(f"John has a child named {p}")


if __name__ == '__main__':
    parent = Person("John")
    child1 = Person("Child 1")
    child2 = Person("Child 2")
    relationships = Relationships()
    relationships.add_parent_child(parent, child1)
    relationships.add_parent_child(parent, child2)
    Research(relationships)
