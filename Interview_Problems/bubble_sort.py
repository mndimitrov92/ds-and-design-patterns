def bubble_sort():  # O(N**2) running time complexity
    arr = [1, 5, 2, 10, 65, 7, 34, 22, 8, 56, 100, 0, -5]
    for x in range(len(arr)):
        for y in range(1, len(arr) - x):  # exclude the last elements
            # if the previous element is grater than the current element
            if arr[y - 1] > arr[y]:
                # Store the higher value in a temp variable
                temp = arr[y - 1]
                # Swap the items by assigning the lower value to the previous element
                arr[y - 1] = arr[y]
                # And then assign the higher value to the current element
                arr[y] = temp
    print("Array was sorted:")
    print(arr)


bubble_sort()
