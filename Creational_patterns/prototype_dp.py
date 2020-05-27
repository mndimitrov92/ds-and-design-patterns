"""
Prototype design pattern

INTENT:
    Prototype is a creational design pattern that lets you copy existing objects without making your
    code dependent on their classes.
APPLICABILITY:
    *Use the Prototype pattern when your code shouldn’t depend on the concrete classes of objects that you need to copy.
    *Use the pattern when you want to reduce the number of subclasses that only differ in the way they initialize their
     respective objects. Somebody could have created these subclasses to be able to create objects with a specific configuration.
PROS AND CONS:
    PROS:
        *You can clone objects without coupling to their concrete classes.
        *You can get rid of repeated initialization code in favor of cloning pre-built prototypes.
        *You can produce complex objects more conveniently.
        *You get an alternative to inheritance when dealing with configuration presets for complex objects.
    CONS:
        *Cloning complex objects that have circular references might be very tricky.
USAGE:
    The Prototype pattern is available in Python out of the box with a Cloneable interface.
IDENTIFICATION:
     The prototype can be easily recognized by a clone or copy methods, etc.
"""
import copy


##################### Prototype #######################
class Address:
    def __init__(self, street, city, country):
        self.city = city
        self.street = street
        self.country = country

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} lives in {self.address}"


# The prototype pattern can be implemented by pythons copy module
def test_prototype():
    john = Person("John", Address("123", "London", "UK"))
    # Recursively copies all attributes from John
    jane = copy.deepcopy(john)
    jane.address.country = "Wales"
    jane.name = "Jane"

    # There is a shallow copy, which in this case copies the address as a reference, which means that both John and
    # Jane 2 will reference the same address
    jane2 = copy.copy(john)
    jane2.name = "Jane 2"
    jane2.address.country = "Ireland"  # Changing the address here will change the country for John as well

    print(john)
    print(jane)
    print(jane2)


######################## Prototype factory #################
class Address2:
    def __init__(self, street, city, suite):
        self.street = street
        self.city = city
        self.suite = suite

    def __str__(self):
        return f"{self.street}, {self.city}, Suite #{self.suite}"


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} works at {self.address}"


class EmployeeFactory:
    # Prototypes
    main_office_employee = Employee("", Address2("4567 Street", "London", 0))
    aux_office_employee = Employee("", Address2("1234 Street", "London", 0))

    @staticmethod
    def __new_employee(proto, name, suite):
        # Clone and update the attributes
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name,
            suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name,
            suite
        )


def test_prototype_factory():
    john = EmployeeFactory.new_main_office_employee("Jane", 101)
    jane = EmployeeFactory.new_aux_office_employee("John", 121)
    print(john)
    print(jane)


#################
# Copy the line object that contains the same start and end points
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        # another way to clone the line
        new_start = Point(self.start.x, self.start.y)
        new_end = Point(self.end.x, self.end.y)
        return Line(new_start, new_end)

    def __str__(self):
        return f"{self.start.x}:{self.start.y} \t {self.end.x}:{self.end.y}"


def test_line_copy():
    l = Line(Point(1, 2), Point(3, 4))
    print(l)
    l2 = l.deep_copy()
    l2.start.x = 6
    print(l2)


if __name__ == '__main__':
    print("Prototype:")
    # test_prototype()
    print("Prototype factory:")
    # test_prototype_factory()
    print("Line copy")
    test_line_copy()
