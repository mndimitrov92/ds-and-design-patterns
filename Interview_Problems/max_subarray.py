# Kadane's algorithm to find the subarray with the maximum sum

test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#                  =========== The max subarray is

def sub_arr(arr):
    current = 0
    answer = 0
    for item in arr:
        current += item
        # Get the maximum value between the current value and the sum so far
        answer = max(answer, current)
        # If the value is negative,  exclude it
        current = max(current, 0)
    return answer


print(sub_arr(test))
