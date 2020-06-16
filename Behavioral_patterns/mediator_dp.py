"""
Mediator design pattern

Facilitates communication between components without them necessarily being aware of each other.

INTENT:
    Mediator is a behavioral design pattern that lets you reduce chaotic dependencies between objects. The pattern
    restricts direct communications between the objects and forces them to collaborate only via a mediator object.
APPLICABILITY:
    * Use the Mediator pattern when it’s hard to change some of the classes because they are tightly coupled to a bunch of other classes.
    * Use the pattern when you can’t reuse a component in a different program because it’s too dependent on other components.
    * Use the Mediator when you find yourself creating tons of component subclasses just to reuse some basic behavior in various contexts.
PROS AND CONS:
    PROS:
        * Single Responsibility Principle. You can extract the communications between various components into a
         single place, making it easier to comprehend and maintain.
        * Open/Closed Principle. You can introduce new mediators without having to change the actual components.
        *You can reduce coupling between various components of a program.
        * You can reuse individual components more easily.
    CONS:
        * Over time a mediator can evolve into a God Object.
USAGE:
    The most popular usage of the Mediator pattern in Python code is facilitating communications between GUI components
     of an app. The synonym of the Mediator is the Controller part of MVC pattern.
"""


# Chat room example with a chat room
class Person:
    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.room = None

    def receive(self, sender, msg):
        s = f"{sender}: {msg}"
        print(f"{self.name}\'s chat session: {s}")
        self.chat_log.append(s)

    def say(self, msg):
        self.room.broadcast(self.name, msg)

    def private_message(self, who, message):
        self.room.message(self.name, who, message)


class ChatRoom:
    """The chat room is the central mediator in this case"""

    def __init__(self):
        self.people = []

    def join_(self, person):
        join_msg = f"{person.name} joins the chat"
        self.broadcast("room", join_msg)
        person.room = self
        self.people.append(person)

    def broadcast(self, source, msg):
        for p in self.people:
            if p.name != source:
                p.receive(source, msg)

    def message(self, source, destination, message):
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)


def test_classic_mediator():
    # Initialize the room
    room = ChatRoom()
    # Create a few people
    john = Person("John")
    jane = Person("Jane")
    # add them to the room
    room.join_(john)
    room.join_(jane)

    john.say("Hi room")
    jane.say("Hi John")

    simon = Person("Simon")
    room.join_(simon)
    simon.say("Hi")

    jane.private_message("Simon", "hi Simon")


# Event mediator in which case the object subscribe to events
# Event - A list of function that you can call one after the other
class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


# Mediator
class Game:
    def __init__(self):
        self.events = Event()

    def fire(self, args):
        self.events(args)


class GoalScoredInfo:
    def __init__(self, who_scored, goals_scored):
        self.who_scored = who_scored
        self.goals_scored = goals_scored


class Player:
    def __init__(self, name, game):
        self.game = game
        self.name = name
        self.goals_scored = 0

    def score(self):
        self.goals_scored += 1
        args = GoalScoredInfo(self.name, self.goals_scored)
        # Use the mediator
        self.game.fire(args)


class Coach:
    def __init__(self, game):
        game.events.append(self.celebrate_goal)

    def celebrate_goal(self, args):
        if isinstance(args, GoalScoredInfo) and args.goals_scored < 3:
            print(f"Coach says: well done {args.who_scored}")


def test_event_mediator():
    game = Game()
    # add the player and coach to the game
    player = Player("Tom", game)
    coach = Coach(game)
    player.score()
    player.score()
    player.score()


if __name__ == '__main__':
    print("Classic mediator:")
    # test_classic_mediator()
    print("Event mediator:")
    test_event_mediator()
