"""
Given 2 arrays (no duplicates)
is array 1 a rotation of another - True / False
same size and elements but start index is different

O(n) are going through each array 2x but O(2n) = O(n)
Select an indexed position in list 1 and get ist value. Find same element in list2 and check index for index in there
if any variation then -> False
Getting the last item without a False is True
"""


def rotation(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    key = arr1[0]
    key_index = 0
    for i in range(len(arr2)):
        if arr2[i] == key:
            key_index = i
            break
    if key_index == 0:
        return False
    for x in range(len(arr1)):
        arr2_index = (key_index + x) % len(arr1)

        if arr1[x] != arr2[arr2_index]:
            return False
    return True


print(rotation([1, 2, 3, 4], [3, 4, 1, 2]))
