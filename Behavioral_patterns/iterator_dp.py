"""
Iterator design pattern

A class that facilitates the traversal of a data structure.

INTENT:
    Iterator is a behavioral design pattern that lets you traverse elements of a collection without exposing
     its underlying representation (list, stack, tree, etc.).
APPLICABILITY:
    *Use the Iterator pattern when your collection has a complex data structure under the hood, but you want to hide
     its complexity from clients (either for convenience or security reasons).
    *Use the pattern to reduce duplication of the traversal code across your app.
    *Use the Iterator when you want your code to be able to traverse different data structures or when types of these
     structures are unknown beforehand.

PROS AND CONS:
    PROS:
        * Single Responsibility Principle. You can clean up the client code and the collections by extracting bulky
        traversal algorithms into separate classes.
        *Open/Closed Principle. You can implement new types of collections and iterators and pass them to existing
         code without breaking anything.
        *You can iterate over the same collection in parallel because each iterator object contains its own iteration state.
        *For the same reason, you can delay an iteration and continue it when needed.
    CONS:
        * Applying the pattern can be an overkill if your app only works with simple collections.
        * Using an iterator may be less efficient than going through elements of some specialized collections directly.
USAGE:
     The pattern is very common in Python code. Many frameworks and libraries use it to provide a standard way for
     traversing their collections.
IDENTIFICATION:
    Iterator is easy to recognize by the navigation methods (such as next, previous and others). Client code that uses
    iterators might not have direct access to the collection being traversed.
"""


# Traversing a simple binary tree
#     1
#    / \
#   2   3

# Create the tree
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

        self.parent = None
        # If there are left or right sub elements, initialize directly the current node as the parent
        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    # One of the ways to expose the iterator
    def __iter__(self):
        return InOrderIterator(self)


# Different types of traversal of the tree
# in-order traversal -> 213 (from left to right)
# pre-order -> 123
# post-order -> 231

# Iterator for the in order traversal
class InOrderIterator:
    def __init__(self, root):
        self.root = self.current = root
        # current will refer the current element
        self.yielded_start = False
        # start from the left most element
        while self.current.left:
            self.current = self.current.left

    def __next__(self):
        if not self.yielded_start:
            self.yielded_start = True
            return self.current

        if self.current.right:
            self.current = self.current.right
            while self.current.left:
                self.current = self.current.left
            return self.current
        else:
            p = self.current.parent
            while p and self.current == p.right:
                self.current = p
                p = p.parent
            self.current = p
            if self.current:
                return self.current
            else:
                raise StopIteration


def traverse_in_order(root):
    def traverse(current):
        if current.left:
            for left in traverse(current.left):
                yield left
        yield current

        if current.right:
            for right in traverse(current.right):
                yield right

    for node in traverse(root):
        yield node


if __name__ == '__main__':
    print("Iterator:")
    # In this example we will traverse in order
    # First, create the tree
    root = Node(1, Node(2), Node(3))

    # calling tbe iterator explicitly
    it = iter(root)
    print([next(it).value for x in range(3)])
    # calling it implicitly
    for x in root:
        print(x.value, end=" | ")
    print("\n")
    for y in traverse_in_order(root):
        print(y.value, end=" | ")
