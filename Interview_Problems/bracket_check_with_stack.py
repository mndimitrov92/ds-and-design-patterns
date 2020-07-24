"""
Given a string made up of the following brackets () {} [] ,determine whether the brackets properly match
"""


def get_rev_bracket(left_bracket):
    brackets = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    return brackets[left_bracket]


def is_left_bracket(bracket):
    return bracket in ["(", "[", "{"]


def bracket_check(string):
    stack = []
    for bracket in string:
        # If it is a left bracket, add it to the stack
        if is_left_bracket(bracket):
            stack.append(bracket)
        elif not len(stack) or (get_rev_bracket(stack.pop()) != bracket):
            return False
    # If stack is empty, then all brackets match properly
    return not stack


invalid = "[{})[]"
valid = "[[{}]()]"
print(bracket_check(invalid))
print(bracket_check(valid))
