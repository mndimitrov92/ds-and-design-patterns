"""
Interpreter design pattern

It is a component that processes structured text data . Does so by turning it into separate lexical tokens(lexing)
and then interpreting sequences of said tokens(parsing)

Mainly used for textual input that needs processing.

The idea is to turn strings into OOP based structures in a complicated process
"""

from enum import Enum, auto


class Token:
    class Type(Enum):
        # Token types
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        LPAREN = auto()
        RPAREN = auto()

    def __init__(self, type_, text):
        self.type_ = type_
        self.text = text

    def __str__(self):
        return f"`{self.text}`"


# The first part of the interpreter pattern (lexing)
# The lexing process has to split and expression into tokens
def lex(input_):
    result = []
    print("Lexing")
    i = 0
    while i < len(input_):
        if input_[i] == "+":
            result.append(Token(Token.Type.PLUS, "+"))
        elif input_[i] == "-":
            result.append(Token(Token.Type.MINUS, "-"))
        elif input_[i] == "(":
            result.append(Token(Token.Type.LPAREN, "("))
        elif input_[i] == ")":
            result.append(Token(Token.Type.RPAREN, ")"))
        else:
            # This is the case where we find an integer
            digits = [input_[i]]
            # Capture the digits
            for j in range(i + 1, len(input_)):
                if input_[j].isdigit():
                    digits.append(input_[j])
                    i += 1
                else:
                    result.append(Token(Token.Type.INTEGER, "".join(digits)))
                    break
        i += 1
    return result


# The second part of the interpreter pattern (parsing)
class Integer:
    def __init__(self, value):
        self.value = value


class BinaryExpression:
    class Type(Enum):
        ADDITION = auto()
        SUBTRACTION = auto()

    def __init__(self):
        self.type_ = None
        self.left = None
        self.right = None

    @property
    def value(self):
        if self.type_ == self.Type.ADDITION:
            return self.left.value + self.right.value
        else:
            return self.left.value - self.right.value


def parse(tokens):
    result = BinaryExpression()
    # Flag to determine the side
    has_left_side = False
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.type_ == Token.Type.INTEGER:
            integer = Integer(int(token.text))
            if not has_left_side:
                result.left = integer
                has_left_side = True
            else:
                result.right = integer
        elif token.type_ == Token.Type.PLUS:
            result.type_ = BinaryExpression.Type.ADDITION
        elif token.type_ == Token.Type.MINUS:
            result.type_ = BinaryExpression.Type.SUBTRACTION
        elif token.type_ == Token.Type.LPAREN:
            j = i
            while j < len(tokens):
                if tokens[j].type_ == Token.Type.RPAREN:
                    break
                j += 1
            subexpression = tokens[i + 1:j]
            element = parse(subexpression)
            if not has_left_side:
                result.left = element
                has_left_side = True
            else:
                result.right = element
            i = j
        i += 1
    return result


def calc(input_):
    tokens = lex(input_)
    print(" ".join(map(str, tokens)))
    parsed = parse(tokens)
    print(f"{input_} = {parsed.value}")


def test_interpreter():
    expression = "(2+3)-(1+3)"
    calc(expression)


if __name__ == '__main__':
    print("Interpreter pattern:")
    test_interpreter()
