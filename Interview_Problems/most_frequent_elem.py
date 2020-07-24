"""
Given an array, what is the most frequently occuring element
"""


def most_frequent(arr):
    count = {}
    max_count = 0
    max_item = None
    for i in arr:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

        if count[i] > max_count:
            max_count = count[i]
            max_item = i
    return max_item


print(most_frequent([1, 2, 4, 5, 6, 4, 3, 4, 4, 4]))
