"""
Template method design pattern

INTENT:
    Template Method is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets
    subclasses override specific steps of the algorithm without changing its structure.
APPLICABILITY:
    *Use the Template Method pattern when you want to let clients extend only particular steps of an algorithm,
    but not the whole algorithm or its structure.
    *Use the pattern when you have several classes that contain almost identical algorithms with some minor differences.
     As a result, you might need to modify all classes when the algorithm changes.
PROS AND CONS:
    PROS:
        *You can let clients override only certain parts of a large algorithm, making them less affected by changes
        that happen to other parts of the algorithm.
        *You can pull the duplicate code into a superclass.
    CONS:
        *Some clients may be limited by the provided skeleton of an algorithm.
        *You might violate the Liskov Substitution Principle by suppressing a default step implementation via a subclass.
        *Template methods tend to be harder to maintain the more steps they have.
USAGE:
    The Template Method pattern is quite common in Python frameworks. Developers often use it to provide framework users
    with a simple means of extending standard functionality using inheritance.
IDENTIFICATION:
    Template Method can be recognized by behavioral methods that already have a “default” behavior defined by the base class.
"""
from abc import ABC


# It is similar to the strategy pattern but uses inheritance instead of composition

class Game(ABC):
    """Base class for a game"""

    def __init__(self, num_of_players):
        self.number_of_players = num_of_players
        self.current_player = 0

    def run(self):
        """This is the general interface for running the game - the template method"""
        self.start()
        while not self.have_winner:
            self.take_turn()
        print(f"Player {self.winning_player} won.")

    # Templates that need to be redefind from the subclasses
    def start(self):
        pass

    @property
    def have_winner(self):
        pass

    def take_turn(self):
        pass

    @property
    def winning_player(self):
        pass


class Chess(Game):
    def __init__(self):
        # Has just 2 players
        super().__init__(2)
        self.max_turns = 10
        self.turn = 1

    def start(self):
        print(f"Starting a game of chess with {self.number_of_players} players")

    @property
    def have_winner(self):
        return self.turn == self.max_turns

    def take_turn(self):
        print(f"Turn {self.turn} taken by player {self.current_player}")
        self.turn += 1
        self.current_player = 1 - self.current_player

    @property
    def winning_player(self):
        return self.current_player


def test_template_method():
    game = Chess()
    game.run()


if __name__ == '__main__':
    print("Template method:")
    test_template_method()
