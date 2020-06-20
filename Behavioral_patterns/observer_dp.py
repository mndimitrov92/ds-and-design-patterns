"""
Observer design pattern

INTENT:
    Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects
     about any events that happen to the object they’re observing.
APPLICABILITY:
    * Use the Observer pattern when changes to the state of one object may require changing other objects,
     and the actual set of objects is unknown beforehand or changes dynamically.
    * Use the pattern when some objects in your app must observe others, but only for a limited time or in specific cases.
PROS AND CONS:
    PROS:
        *Open/Closed Principle. You can introduce new subscriber classes without having to change the publisher’s code
         (and vice versa if there’s a publisher interface).
        *You can establish relations between objects at runtime.
    CONS:
        * Subscribers are notified in random order.
USAGE:
    The Observer pattern is pretty common in Python code, especially in the GUI components. It provides a way to react
     to events happening in other objects without coupling to their classes.
IDENTIFICATION:
    The pattern can be recognized by subscription methods, that store objects in a list and by calls to the
     update method issued to objects in that list.
"""


class Event(list):
    """The observer"""

    def __call__(self, *args, **kwargs):
        # For every subscriber, we call the subscriber
        for item in self:
            item(*args, **kwargs)


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        # attribute that will subscribe the person to the observer (the Event)
        self.is_ill = Event()

    def become_ill(self):
        # method to subscribe to the observer
        self.is_ill(self.name, self.address)


def call_a_doc(name, address):
    print(f"{name} needs a doctor at {address}")


def test_observer():
    person = Person("Tom", "22 Ave")
    # subscribe the doctor to the event
    person.is_ill.append(call_a_doc)
    # invoke the event
    person.become_ill()
    # unsubscribe call_doctor to the event
    person.is_ill.remove(call_a_doc)
    person.become_ill()


# Property observer
class PropertyObservable:
    def __init__(self):
        # will just have an event that people could subscribe to
        self.property_changed = Event()


class NewPerson(PropertyObservable):
    def __init__(self, age=0):
        super().__init__()
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if self._age == value:
            return
        self._age = value
        # perform the property changed notification
        self.property_changed('age', value)


class TrafficAuthority:
    def __init__(self, person):
        self.person = person
        # subscribe to the property changed event
        person.property_changed.append(self.person_changed)

    def person_changed(self, name, value):
        """Method for handling the property change"""
        if name == 'age':
            if value < 18:
                print("You still cannot drive")
            else:
                print("You can drive now!")
                # Remove the subscription here
                self.person.property_changed.remove(self.person_changed)


def test_property_observer():
    person = NewPerson()
    # subscribe to the person
    ta = TrafficAuthority(person)
    # Change the age
    for age in range(14, 22):
        print(f"Setting age to {age}")
        person.age = age


if __name__ == '__main__':
    print("Observer:")
    test_observer()

    print("Property observer:")
    test_property_observer()
