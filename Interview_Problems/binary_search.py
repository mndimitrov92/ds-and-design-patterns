# Binary search example -> O(log(n))
test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binary_search(arr, value):
    start = 0  # First position
    end = len(arr) - 1  # Last position
    while start <= end:
        middle = (start + end) // 2  # Capture the middle
        if value == arr[middle]:  # If the value is equal to the current center value of the array
            return arr[middle]
        elif value < arr[middle]:
            end = middle - 1  # The end point is now updated to reference the middle elem of the current array -1
        elif value > arr[middle]:
            start = middle + 1  # The start point is now updated to reference the middle elem of the current array +1


print(binary_search(test_arr, 6))
