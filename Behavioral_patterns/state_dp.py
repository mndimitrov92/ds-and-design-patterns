"""
State design pattern

INTENT:
    State is a behavioral design pattern that lets an object alter its behavior when its internal state changes.
     It appears as if the object changed its class.
APPLICATION:
    *Use the State pattern when you have an object that behaves differently depending on its current state, the number
     of states is enormous, and the state-specific code changes frequently.
    *Use the pattern when you have a class polluted with massive conditionals that alter how the class behaves
     according to the current values of the class’s fields.
    *Use State when you have a lot of duplicate code across similar states and transitions of a condition-based state machine.
PROS AND CONS:
    PROS:
        *Single Responsibility Principle. Organize the code related to particular states into separate classes.
        *Open/Closed Principle. Introduce new states without changing existing state classes or the context.
        *Simplify the code of the context by eliminating bulky state machine conditionals.

    CONS:
        *Applying the pattern can be overkill if a state machine has only a few states or rarely changes.
USAGE:
    The State pattern is commonly used in Python to convert massive switch-base state machines into the objects.
IDENTIFICATION:
    State pattern can be recognized by methods that change their behavior depending on the objects’ state, controlled externally.
"""

from abc import ABC
from enum import Enum, auto


# Classic implementation of the pattern
class Switch:
    def __init__(self):
        self.state = OffState()

    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)


class State(ABC):
    def on(self, switch):
        print("Light is ON")

    def off(self, switch):
        print("Light is OFF")


# Every state in the patter is actually a separate class which are being invoked based on the state
# of the Switch class
class OnState(State):
    def __init__(self):
        print("Light is turned on")

    def off(self, switch):
        print("We are turning the light off...")
        switch.state = OffState()


class OffState(State):
    def __init__(self):
        print("Light is turned off")

    def off(self, switch):
        print("We are turning the light on...")
        # The method transition to the different state
        switch.state = OnState()


def test_classic_state():
    sw = Switch()
    sw.on()
    sw.off()
    sw.off()


# State machine
class State(Enum):
    OFF_HOOK = auto()
    CONNECTING = auto()
    CONNECTED = auto()
    ON_HOLD = auto()
    ON_HOOK = auto()


# Triggers
class Trigger(Enum):
    """The class that causes the transition"""
    CALL_DIALED = auto()
    CALL_CONNECTED = auto()
    HANG_UP = auto()
    PLACED_ON_HOLD = auto()
    TAKEN_OFF_HOLD = auto()
    LEFT_MESSAGE = auto()


def test_state_machine():
    rules = {
        # For each state define the transition and next state
        State.OFF_HOOK: [
            (Trigger.CALL_DIALED, State.CONNECTING)
        ],
        State.CONNECTING: [
            (Trigger.HANG_UP, State.ON_HOOK),
            (Trigger.CALL_CONNECTED, State.CONNECTED)
        ],
        State.CONNECTED: [
            (Trigger.LEFT_MESSAGE, State.ON_HOOK),
            (Trigger.HANG_UP, State.ON_HOOK),
            (Trigger.PLACED_ON_HOLD, State.ON_HOLD)
        ],
        State.ON_HOLD: [
            (Trigger.TAKEN_OFF_HOLD, State.CONNECTED),
            (Trigger.HANG_UP, State.ON_HOOK)
        ]
    }
    # Starting state
    state = State.OFF_HOOK
    # Exit state
    exit_state = State.ON_HOOK

    while state != exit_state:
        print(f"The phone is currently {state}")

        for i in range(len(rules[state])):
            trigger = rules[state][i][0]
            print(f"{i}: {trigger}")
        idx = int(input("Select a trigger:"))
        s = rules[state][idx][1]
        state = s
    print("We are done!")


if __name__ == '__main__':
    print("Classic State:")
    test_classic_state()
    print("State machine:")
    test_state_machine()
