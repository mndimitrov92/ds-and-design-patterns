"""
Flyweight design pattern

INTENT:
    Flyweight is a structural design pattern that lets you fit more objects into the available amount of RAM by sharing
    common parts of state between multiple objects instead of keeping all of the data in each object.
    Generally it is a space optimization technique that lets us use less memory by storing externally the data
    associated with similar objects.
APPLICABILITY:
    Use the Flyweight pattern only when your program must support a huge number of objects which barely fit into available RAM.
    The benefit of applying the pattern depends heavily on how and where it’s used. It’s most useful when:

    *an application needs to spawn a huge number of similar objects
    *this drains all available RAM on a target device
    *the objects contain duplicate states which can be extracted and shared between multiple objects
PROS AND CONS:
    PROS:
        *You can save lots of RAM, assuming your program has tons of similar objects.
    CONS:
        *You might be trading RAM over CPU cycles when some of the context data needs to be recalculated each time somebody calls a flyweight method.
        *The code becomes much more complicated. New team members will always be wondering why the state of an entity was separated in such a way.
USAGE:
    The Flyweight pattern has a single purpose: minimizing memory intake. If your program doesn’t struggle
     with a shortage of RAM, then you might just ignore this pattern for a while.
IDENTIFICATION:
    Flyweight can be recognized by a creation method that returns cached objects instead of creating new.
"""
import random
import string


def random_string():
    """Generate a random string with 8 characters that will be used for the first and last name of the user"""
    chars = string.ascii_lowercase
    return "".join([random.choice(chars) for x in range(8)])


# First Flyweight example for storing user names
class User:
    """Ordinary class """

    def __init__(self, name):
        self.name = name


class UserWithFlyweight:
    # we first need a static variable to store the inputs
    strings = []

    def __init__(self, name):
        self.names = [self.get_or_add(x) for x in name.split(" ")]

    def get_or_add(self, s):
        if s in self.strings:
            # get the index of the string if it is present
            return self.strings.index(s)
        else:
            # otherwise append it
            self.strings.append(s)
            return len(self.strings) - 1

    def __str__(self):
        return " ".join([self.strings[x] for x in self.names])


def test_user_generation():
    # Usage without the flyweight pattern
    users = []
    first_names = [random_string() for _ in range(100)]
    last_names = [random_string() for _ in range(100)]
    # Generate 10 000 users with the ordinary class
    for first in first_names:
        for last in last_names:
            users.append(User(f"{first} {last}"))

    # Test Flyweight
    u1 = UserWithFlyweight("Jim Jones")
    u2 = UserWithFlyweight("Tom Jones")
    print(u1.names)
    print(u2.names)
    print(UserWithFlyweight.strings)

    flyweight_users = []
    for first in first_names:
        for last in last_names:
            flyweight_users.append(UserWithFlyweight(f"{first} {last}"))


# Using Flyweight for text formatting
class RegularTextFormatter:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        # Create an array with bool values for capitalization corresponding to each letter of the text
        self.caps = [False] * len(self.plain_text)

    def capitalize(self, start, end):
        """Sets the capitalization marker of the letters in a given range"""
        for x in range(start, end):
            self.caps[x] = True

    def __str__(self):
        result = []
        for x in range(len(self.plain_text)):
            # Capture the current character
            c = self.plain_text[x]
            # append the uppercased version if the marker in the caps array is True
            result.append(c.upper() if self.caps[x] else c)

        return "".join(result)


class FlyweightTextFormatter:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        # A variable to store the formatting
        self.formatting = []

    # Create the flyweight inner class
    class TextRange:
        def __init__(self, start, end, capitalize=False, bold=False, italic=False):
            self.start = start
            self.end = end
            self.capitalize = capitalize
            self.bold = bold
            self.italic = italic

        def covers(self, position):
            """Check if the given position is within the range"""
            return self.start <= position <= self.end

    def get_range(self, start, end):
        char_range = self.TextRange(start, end)
        # Add the character range in the formatting variable
        self.formatting.append(char_range)
        return char_range

    def __str__(self):
        result = []
        for x in range(len(self.plain_text)):
            c = self.plain_text[x]
            for r in self.formatting:
                # If the letter is in the given range and has the capitalization flag, change it to uppercased
                if r.covers(x) and r.capitalize:
                    c = c.upper()
                result.append(c)
        return "".join(result)


def test_text_formatter():
    some_text = "This is a nice place."
    rtf = RegularTextFormatter(some_text)
    rtf.capitalize(5, 7)
    print(rtf)

    # Flyweight text formatter
    ftf = FlyweightTextFormatter(some_text)
    # set the capitalize flag for this range to True
    ftf.get_range(10, 15).capitalize = True
    print(ftf)


# Third flyweight exercise
# Given a string of words we need to create an interface to capitalize particular words from the string
class Sentence:
    def __init__(self, text):
        # Split the text into words
        self.text = text.split(" ")
        # Variable to hold the words
        self.words = {}

    class Word:
        """Flyweight to """

        def __init__(self, capitalize=False):
            self.capitalize = capitalize

    def __getitem__(self, item):
        word = self.Word()
        # Add the marker to the dictionary and return it
        self.words[item] = word
        return self.words[item]

    def __str__(self):
        result = []
        for i, w in enumerate(self.text):
            # If the index of the word is in the dictionary and the words has the capitalize marker
            if i in self.words and self.words[i].capitalize:
                # Capitalize the word
                w = w.upper()
            # Append the output to the result
            result.append(w)
        return " ".join(result)


def test_word_capitalizer():
    text = "Hello world"
    s = Sentence(text)
    # Capitalize the word on index 1
    s[1].capitalize = True
    print(s)


if __name__ == '__main__':
    print("Test flyweight with user names:")
    # test_user_generation()

    print("Flyweight example with text formatting:")
    test_text_formatter()

    print("Test flyweight example 3:")
    test_word_capitalizer()