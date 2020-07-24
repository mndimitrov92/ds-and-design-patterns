"""
Take an array with positive and negative integers and find the maximum running sum of that array
"""


def largest_sum(arr):
    if len(arr) == 0:
        return print("Array too small")
	# Assign the max sum and the current sum to be the first element
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum


print(largest_sum([5, 4, -2, 3, 4, -6, 12, -9]))
