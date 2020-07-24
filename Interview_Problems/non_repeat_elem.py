"""
Non repeat element
Take a string and return a character that never repeats
if multiple uniques then return only the first unique
"""


def repeating(s):
    s = s.replace(" ", "").lower()
    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # IF all uniques are needed
    # return [char for char in s if char_count[char] == 1]

    # return only the first unique item
    for char in s:
        if char_count[char] == 1:
            return char
    return None


print(repeating("I apple ape peels"))
