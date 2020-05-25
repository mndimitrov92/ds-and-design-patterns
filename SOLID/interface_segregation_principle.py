"""
Interface segregation principle
A client should not be forced to depend on methods it does not use.
Idea is to not stick too many methods in an interface
"""
from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


# For this class the interface is OK
class MultifunctionalPrinter(Machine):
    def print(self, document):
        # Do something
        pass

    def fax(self, document):
        # Do something
        pass

    def scan(self, document):
        # Do something
        pass


# For this one, which does not need all the methods, it is not
# In the below case the unneeded methods are still there and need to be handled
# but their presence is still misleading
class OldPrinter(Machine):
    def print(self, document):
        # Do something
        pass

    def scan(self, document):
        # One approach is to pass the unneeded methods
        pass

    def fax(self, document):
        # Another way is to raise an error that it is not supported
        raise NotImplementedError("Not supported")


# The proper way is to split the machine interface into more granular ones
# which will only be used where needed
class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scnner:
    @abstractmethod
    def scan(self, document):
        pass


class Fax:
    @abstractmethod
    def fax(self, document):
        pass


class SimplePrinter(Printer):
    def print(self, document):
        pass  # print implementation


# When you need to have a combination
class Photocopier(Printer, Scnner):
    def print(self, document):
        pass  # override the method

    def scan(self, document):
        pass  # override the method
