"""
Memento design pattern

INTENT:
    Memento is a behavioral design pattern that lets you save and restore the previous state of an object without
    revealing the details of its implementation.
APPLICABILITY:
    * Use the Memento pattern when you want to produce snapshots of the object’s state to be able to restore
    a previous state of the object.
    *Use the pattern when direct access to the object’s fields/getters/setters violates its encapsulation.
PROS AND CONS:
    PROS:
        *You can produce snapshots of the object’s state without violating its encapsulation.
        *You can simplify the originator’s code by letting the caretaker maintain the history of the originator’s state.
    CONS:
        *The app might consume lots of RAM if clients create mementos too often.
        *Caretakers should track the originator’s lifecycle to be able to destroy obsolete mementos.
        *Most dynamic programming languages, such as PHP, Python and JavaScript, can’t guarantee that the state within
         the memento stays untouched.
USAGE:
    The Memento’s principle can be achieved using the serialization, which is quite common in Python. While it’s
    not the only and the most efficient way to make snapshots of an object’s state, it still allows storing state
     backups while protecting the originator’s structure from other objects.
"""


class Memento:
    def __init__(self, balance):
        # Here we specify all the particulars of the object to be snapshot, in this just the balance
        self.balance = balance


class BankAccount:
    """In this case we do not store the initial state of the object"""

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        # Here we return a snapshot of the current state of the object
        return Memento(self.balance)

    # the point of the mementos is to rollback the system into a previous state
    def restore(self, memento):
        self.balance = memento.balance

    def __str__(self):
        return f"Balance = {self.balance}"


class BankAccountRedo:
    """Implementing it this way will allow undo and redo functionality"""

    def __init__(self, balance=0):
        self.balance = balance
        # In order to have undo and redo functionality and store the initial state
        # we can store the mementos in a list where we start with an initial memento
        self.changes = [Memento(self.balance)]
        # pointer to the state
        self.current = 0

    def deposit(self, amount):
        self.balance += amount
        # Here append the memento to the mementos list and increment the pointer
        m = Memento(self.balance)
        self.changes.append(m)
        self.current += 1
        # after that we return the memento
        return m

    # the point of the mementos is to rollback the system into a previous state
    def restore(self, memento):
        # Guard condition if the memento is not None
        if memento:
            # Change the balance and append the memento to the list
            self.balance = memento.balance
            self.changes.append(memento)
            # the pointer to the last element of the list
            self.current = len(self.changes) - 1

    def undo(self):
        if self.current > 0:
            # decrease the pointer
            self.current -= 1
            # get the memento
            m = self.changes[self.current]
            self.balance = m.balance
            return m
        # if we fail to redo
        return None

    def redo(self):
        if self.current + 1 < len(self.changes):
            self.current += 1
            m = self.changes[self.current]
            self.balance = m.balance
            return m
        return None

    def __str__(self):
        return f"Balance = {self.balance}"


def test_memento():
    ba = BankAccount(100)
    # Two mementos to store the different deposits
    m1 = ba.deposit(50)
    m2 = ba.deposit(25)
    print(ba)
    # Restore to m1 state
    ba.restore(m1)
    print(ba)
    # In this case,however we don't have the memento for the initial state


def test_memento_undo_redo():
    ba = BankAccountRedo(100)
    # Two mementos to store the different deposits
    m1 = ba.deposit(50)
    m2 = ba.deposit(25)
    print(ba)

    ba.undo()
    print(f"Undo 1: {ba}")
    ba.undo()
    print(f"Undo 2: {ba}")
    ba.redo()
    print(f"Redo 1: {ba}")

if __name__ == '__main__':
    print("Memento:")
    test_memento()
    print("Memento with undo/redo:")
    test_memento_undo_redo()
