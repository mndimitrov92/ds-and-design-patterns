"""
Command design pattern

INTENT:
    Command is a behavioral design pattern that turns a request into a stand-alone object that contains
    all information about the request. This transformation lets you parameterize methods with different requests,
    delay or queue a request’s execution, and support undoable operations.
APPLICABILITY:
    * Use the Command pattern when you want to parametrize objects with operations.
    * Use the Command pattern when you want to queue operations, schedule their execution, or execute them remotely.
    * Use the Command pattern when you want to implement reversible operations.
PROS AND CONS:
    PROS:
        *Single Responsibility Principle. You can decouple classes that invoke operations from classes that perform these operations.
        *Open/Closed Principle. You can introduce new commands into the app without breaking existing client code.
        *You can implement undo/redo.
        *You can implement deferred execution of operations.
        *You can assemble a set of simple commands into a complex one.
    CONS:
        *The code may become more complicated since you’re introducing a whole new layer between senders and receivers.
USAGE:
    The Command pattern is pretty common in Python code. Most often it’s used as an alternative for callbacks to
    parameterizing UI elements with actions. It’s also used for queueing tasks, tracking operations history, etc.
IDENTIFICATIONS:
    The Command pattern is recognizable by behavioral methods in an abstract/interface type (sender) which
    invokes a method in an implementation of a different abstract/interface type (receiver) which has been encapsulated
    by the command implementation during its creation. Command classes are usually limited to specific actions.
"""
from enum import Enum
from abc import ABC


# Command pattern
class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully, balance is now: {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount > BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"{amount} withdrawn successfully, balance is now: {self.balance}")
            return True  # Operation Successfully performed
        return False

    def __str__(self):
        return f"Current balance: {self.balance}"


class Command(ABC):
    """Abstract class for the commands"""
    def __init__(self):
        # A flag for successful operation (unsuccessful one is considered when you withdraw an amount > current balance)
        self.success = False

    def invoke(self):
        pass

    def undo(self):
        pass


class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, account, action, amount):
        super().__init__()
        self.account = account
        self.action = action
        self.amount = amount

    def invoke(self):
        # Call the command
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            # Store the result of the withdraw operation
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        # if the invoked command did not succeed, simply return because there will be nothing to undo
        if not self.success:
            return
        # in this case undoing an operation will mean performing the opposite action with the same amount
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


def test_command():
    ba = BankAccount()
    # Instead of calling withdraw or deposit on this object, we have the bank account command
    cmd = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
    # call the command
    cmd.invoke()
    print(f"After invoking the command: {ba}")
    # Undoing the command
    cmd.undo()
    print(f"After undoing the command: {ba}")

    # Impossible command
    cmd2 = BankAccountCommand(ba, BankAccountCommand.Action.WITHDRAW, 1000)
    # call the command
    cmd2.invoke()
    print(f"After invoking the impossible command: {ba}")
    # Undoing the command
    cmd2.undo()
    print(f"After undoing the impossible command: {ba}")


# Composite command
class CompositeBankAccountCommand(Command, list):
    """Composite class that runs all the command consecutively"""

    def __init__(self, items=[]):
        super().__init__()
        # Populate the list the the pending commands
        for item in items:
            self.append(item)

    def invoke(self):
        # execute the commands one after the other
        for cmd in self:
            cmd.invoke()

    def undo(self):
        # Call the commands in reversed order
        for cmd in reversed(self):
            cmd.undo()


def test_composite_command():
    ba = BankAccount()

    deposit1 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
    deposit2 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 200)

    # after the commands have been created, pass them to the composite command
    composite_cmd = CompositeBankAccountCommand([deposit1, deposit2])
    # then call the invoke methods of the commands
    composite_cmd.invoke()
    print(ba)
    print("Undoing....")
    composite_cmd.undo()
    print(ba)


if __name__ == '__main__':
    print("Test command pattern:")
    # test_command()

    print("Composite command:")
    test_composite_command()
