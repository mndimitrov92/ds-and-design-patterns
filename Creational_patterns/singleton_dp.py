"""
Singleton design pattern
INTENT:
    Singleton is a creational design pattern that lets you ensure that a class has only one instance,
    while providing a global access point to this instance.
APPLICABILITY:
    *Use the Singleton pattern when a class in your program should have just a single instance available to all clients;
    for example, a single database object shared by different parts of the program.
    *Use the Singleton pattern when you need stricter control over global variables.
PROS AND CONS:
    PROS:
        *You can be sure that a class has only a single instance.
        *You gain a global access point to that instance.
        *The singleton object is initialized only when it’s requested for the first time.
    CONS:
        *Violates the Single Responsibility Principle. The pattern solves two problems at the time.
        *The Singleton pattern can mask bad design, for instance, when the components of the program know too much about each other.
        *The pattern requires special treatment in a multithreaded environment so that multiple threads won’t create a singleton object several times.
        *It may be difficult to unit test the client code of the Singleton because many test frameworks rely on
         inheritance when producing mock objects. Since the constructor of the singleton class is private and overriding
         static methods is impossible in most languages, you will need to think of a creative way to mock the singleton.
         Or just don’t write the tests. Or don’t use the Singleton pattern.
USAGE:
    A lot of developers consider the Singleton pattern an antipattern. That’s why its usage is on the decline in Python code.
IDENTIFICATION:
    Singleton can be recognized by a static creation method, which returns the same cached object.
"""


# First type of Singleton implementation (Singleton allocator)
class SingletonV1:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(SingletonV1, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    # In this case, however the init is being called for each instance
    def __init__(self):
        print("I've been initialized")


def test_singleton_allocator():
    inst1 = SingletonV1()
    inst2 = SingletonV1()
    print(id(inst1) == id(inst2))


# Second type of singleton (Singleton decorator), takes care of the initializer problem
def singleton_v2(class_):
    """Singleton decorator"""
    # Store the class instances in a dictionary
    instances = {}

    def get_instances(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instances


@singleton_v2
class TestClass:
    def __init__(self):
        # Prove that it is being initialized once
        print("Initializing")


def test_singleton_decorator():
    test1 = TestClass()
    test2 = TestClass()
    print(id(test1) == id(test2))


# Third way to implement the Singleton is with a metaclass
# Singleton metaclass
class SingletonV3(type):
    _instances = {}

    # Implementaion is similar to the decorator singleton version
    # and the issue with the initializer is being handler
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonV3, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TestSingletonV3(metaclass=SingletonV3):
    def __init__(self):
        print("Initializing v3")


def test_singleton_meta():
    test1 = TestSingletonV3()
    test2 = TestSingletonV3()
    print(id(test1) == (id(test2)))


# Monostate implementation of Singleton - variation of the singleton pattern
# where you put all the state of the object into a static variable but at the same time allow people to make new objects

class MonostateSingleton:
    # Keep the state in the shared dict
    _shared_attributes = {
        "attr1": "Test",
        "attr2": 42
    }

    def __init__(self):
        # Assign the shared attributes to the class dict
        # Copy the reference to the entire dictionary
        self.__dict__ = self._shared_attributes

    def __str__(self):
        return f"Attribute1: {self.attr1}; Attribute2: {self.attr2}"


def test_monostate_singleton():
    test1 = MonostateSingleton()
    test2 = MonostateSingleton()
    # In this case the objects are different but the attributes are the same
    print(test1 == test2)
    print(test1)
    print(test2)
    # This singleton allows changing the attributes of the instance, however it changes this attribute to all instanes
    test2.attr2 = 69
    print(test1)
    print(test2)


if __name__ == '__main__':
    print("First type of singleton (allocator):")
    # test_singleton_allocator()

    print("Second singleton type (decorator):")
    # test_singleton_decorator()

    print("Third singleton type (with Metaclass):")
    # test_singleton_meta()

    print("Fourth singleton type (monostate):")
    test_monostate_singleton()
