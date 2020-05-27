"""
Builder design pattern
======================
INTENT:
    Builder is a creational design pattern that lets you construct complex objects step by step.
    The pattern allows you to produce different types and representations of an object using the
    same construction code.
APPLICABILITY:
    *Use the Builder pattern to get rid of a “telescopic constructor”.
        Say you have a constructor with ten optional parameters. Calling such a beast is very inconvenient;
        therefore, you overload the constructor and create several shorter versions with fewer parameters.
        These constructors still refer to the main one, passing some default values into any omitted parameters.

        The Builder pattern lets you build objects step by step, using only those steps that you really need.
        After implementing the pattern, you don’t have to cram dozens of parameters into your constructors anymore.
    *Use the Builder pattern when you want your code to be able to create different representations of some product
     (for example, stone and wooden houses).
        The Builder pattern can be applied when construction of various representations of the product involves
        similar steps that differ only in the details.

        The base builder interface defines all possible construction steps, and concrete builders implement
        these steps to construct particular representations of the product. Meanwhile, the director class
        guides the order of construction.
    *Use the Builder to construct Composite trees or other complex objects.
        The Builder pattern lets you construct products step-by-step. You could defer execution of some steps
        without breaking the final product. You can even call steps recursively,
        which comes in handy when you need to build an object tree.
        A builder doesn’t expose the unfinished product while running construction steps.
        This prevents the client code from fetching an incomplete result.
PROS and CONS:
    PROS:
        *You can construct objects step-by-step, defer construction steps or run steps recursively.
        *You can reuse the same construction code when building various representations of products.
        *Single Responsibility Principle. You can isolate complex construction code from the business logic of the product.
    CONS:
        *The overall complexity of the code increases since the pattern requires creating multiple new classes.
USAGE:
    The Builder pattern is a well-known pattern in Python world.
    It’s especially useful when you need to create an object with lots of possible configuration options.
IDENTIFICATION:
    The Builder pattern can be recognized in class, which has a single creation method and several methods
    to configure the resulting object. Builder methods often support chaining:
    obj.method1().method2().method3()...
    This can be done by returning self in the respective method
"""


################ HTML ELEMENT BUILDER #####################
class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f"{i1}{self.text}")

        for element in self.elements:
            lines.append(element.__str(indent + 1))

        lines.append(f"{i}</{self.name}>")
        return "\n".join(lines)

    def __str__(self):
        return self.__str(0)

    # In this case exposing the builder breaks the open closed principle
    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(root_name)

    def add_child(self, child_name, text):
        self.__root.elements.append(
            HtmlElement(child_name, text)
        )

    def add_child_fluent(self, child_name, text):
        """Allows chaining"""
        self.__root.elements.append(
            HtmlElement(child_name, text)
        )
        return self

    def __str__(self):
        return str(self.__root)


def builder_test():
    # builder = HtmlBuilder("ul")
    # builder.add_child("li", "hello")
    # builder.add_child("li", "world")

    builder = HtmlElement.create("ul")
    builder.add_child_fluent("li", "hello").add_child("li", "world")
    print(builder)


############# BUILDER FACETS #######################
# If the object is so complicated to build and the need of several builders is needed
class Person:
    def __init__(self):
        # Address
        self.street = None
        self.postcode = None
        self.city = None
        # Employment
        self.company_name = None
        self.position = None
        self.income = None

    def __str__(self):
        return f"Address: {self.street}, {self.postcode} , {self.city} " + \
               f"Employed at: {self.company_name}, as a {self.position} earning {self.income}."


class PersonBuilder:
    """Base class for the builders"""

    # To avoid constucting blank persons each time, set the default value
    def __init__(self, person=Person()):
        self.person = person

    def build(self):
        return self.person

    # Using the JobBuilder can be done by defining
    # However this also breaks the open closed principle as if new builders are needed this class will need to
    # be updated with new properties
    @property
    def works(self):
        return JobBuilder(self.person)

    @property
    def lives(self):
        return AddressBuilder(self.person)


class JobBuilder(PersonBuilder):
    """Builder for the employment part"""

    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, income):
        self.person.income = income
        return self


class AddressBuilder(PersonBuilder):
    """Builder for the address part"""

    def __init__(self, person):
        super().__init__(person)

    def lives_at(self, address):
        self.person.street = address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


def multi_builders_test():
    person_builder = PersonBuilder()
    person = person_builder.lives \
        .lives_at("Some address") \
        .in_city("Some city") \
        .with_postcode("1234") \
        .works \
        .at("Some companyy") \
        .as_a("Position") \
        .earning("123444") \
        .build()
    print(person)


################### Builder Inheritance ##########
# To avoid braking the open closed principle if using multiple builders
class PersonBuilderV2():
    def __init__(self):
        self.person = PersonV2()

    def build(self):
        return self.person


class PersonV2:
    def __init__(self):
        self.name = None
        self.position = None
        self.date = None

    def __str__(self):
        return f"{self.name} was born on {self.date} and works as {self.position}"

    @staticmethod
    def new():
        return PersonBuilderV2()


class PersonInfoBuilder(PersonBuilderV2):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date):
        self.person.date = date
        return self


def builder_inheritance_test():
    # From the most derived class
    pb = PersonBirthDateBuilder()
    me = pb.called("My name").works("Some job").born("1/1/1111").build()
    print(me)


###################### Code builder ################
class Field:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"self.{self.name} = {self.value}"


class ClassBuilder:
    def __init__(self, class_name):
        self.class_name = class_name
        self.fields = []

    def __str__(self):
        lines = [f"class {self.class_name}"]
        if self.fields:
            lines.append("  def __init__(self):")
            for field in self.fields:
                lines.append("    " + str(field))
        else:
            lines.append("  pass")
        return "\n".join(lines)


class CodeBuilder:
    """Renders simple chunks of code"""
    def __init__(self, name):
        self._class = ClassBuilder(name)

    def __str__(self):
        return self._class.__str__()

    def add_field(self, name, value):
        self._class.fields.append(Field(name, value))
        return self


def test_code_builder():
    cb = CodeBuilder("Person").add_field("name", "''").add_field("age", "14")
    print(cb)


if __name__ == '__main__':
    print("Ordinary builder:")
    # builder_test()
    print("Multi builders:")
    # multi_builders_test
    print("Builders using inheritance:")
    # builder_inheritance_test()
    print("Code builder:")
    test_code_builder()
