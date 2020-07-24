def pair_sum(arr, target):
    """Given an integer array, output all unique pairs that sum up to a specific target value
    In: pair_sum([1,2,3,2], 4)
    Out: (1,3), (2,2)"""
    if len(arr) < 2:
        print("Too small array")

    seen = set()
    output = set()

    for num in arr:
        # Get the remainder to the target
        remainder = target - num
        if remainder not in seen:
            seen.add(num)
        else:
            output.add((min(num, remainder), max(num, remainder)))
    print("\n".join(map(str, list(output))))


pair_sum([1, 3, 2, 2], 4)
