def is_anagram(first, second):
    """Function to check if the strings are anagrams
    Anagram is a string which after shuffling the letters can produce another word which includes all the characters
    Ex: god <-> dog    clint eastwood <-> old west action"""
    first = sorted(first.replace(" ", "").lower())
    second = sorted(second.replace(" ", "").lower())
    return first == second


# Check one
print(is_anagram("dog", "God"))
# Check two
print(is_anagram("aa", "vv"))
# # Check two
print(is_anagram("clint eastwood", "old west action"))
