"""
Facade design pattern

INTENT:
    Facade is a structural design pattern that provides a simplified interface to a library, a framework,
     or any other complex set of classes.
APPLICABILITY:
    *Use the Facade pattern when you need to have a limited but straightforward interface to a complex subsystem.
    *Use the Facade when you want to structure a subsystem into layers.
PROS AND CONS:
    PROS:
        You can isolate your code from the complexity of a subsystem.
    CONS:
        A facade can become a god object coupled to all classes of an app.
USAGE:
    The Facade pattern is commonly used in apps written in Python. It’s especially handy when working with complex libraries and APIs.
IDENTIFICATION:
    Facade can be recognized in a class that has a simple interface, but delegates most of the work to other classes.
    Usually, facades manage full life cycle of objects they use.
"""


# Subsystems for the Facade
class Buffer:
    def __init__(self, width=30, height=60):
        self.width = width
        self.height = height
        self.buffer = [" "] * (self.width * self.height)

    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.buffer += text


class ViewPort:
    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[self.offset + index]

    def append(self, text):
        self.buffer += text


# The facade
class Console():
    def __init__(self):
        b = Buffer()
        self.curr_viewport = ViewPort(b)
        self.buffers = []
        self.viewports = [self.curr_viewport]

    # The facade can expose high-level methods
    def write(self, text):
        self.curr_viewport.buffer.write(text)

    # Or low-level methods from a particular class for power users
    def get_char_at(self, index):
        return self.curr_viewport.get_char_at(index)


if __name__ == '__main__':
    print("Facade demo:")
    col = Console()
    col.write("Test")
    ch = col.get_char_at(0)
    print(ch)
