"""
Common elements in two sorted arrays
Return the common elements between two sorted arrays of integers
EX:  arr1  = [1,3,4,5,6,7,9]
     arr2 = [1,2,4,5,6,10]
Result = [1, 4, 5, 6]
"""


def common_elements(a, b):
    p1 = 0
    p2 = 0
    result = []
    while p1 < len(a) and p2 < len(b):
        if a[p1] == b[p2]:
            result.append(a[p1])
            p1 += 1
            p2 += 2

        elif a[p1] > b[p2]:
            p2 += 1
        else:
            p1 += 1
    return result


print(common_elements([1, 4, 5, 7], [0, 1, 3, 6, 7]))
