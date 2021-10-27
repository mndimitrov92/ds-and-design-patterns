# Write a function fib that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.
# The 0-th number of the sequence is 0.
# The 1-st number of the sequence is 1.
# To generate further numbers of the sequence, calculate the sum of previous two numbers.
# Solve this recursively.
def fib(n):
	"""
	Time: O(2^n)
	Space: O(n)
	"""
	if n <=1:
		return n
	return fib(n-1) + fib(n-2)

assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(4) == 3
assert fib(5) == 5


# Write a function sum_possible that takes in an amount and a list of positive numbers.
# The function should return a boolean indicating whether or not it is possible to create the amount by summing numbers of the list. You may reuse numbers of the list as many times as necessary.
# You may assume that the target amount is non-negative.
def sum_possible(amount, numbers):
	if amount < 0:
		return False
	if amount == 0:
		return True
	for num in numbers:
		if sum_possible(amount - num, numbers):
			return True
	return False

assert sum_possible(8, [5, 12, 4])  == True
assert sum_possible(15, [6, 2, 10, 19]) == False
assert sum_possible(13, [6, 2, 1]) == True
assert sum_possible(103, [6, 20, 1]) == True
assert sum_possible(12, []) == False


# Write a function min_change that takes in an amount and a list of coins.
# The function should return the minimum number of coins required to create the amount. You may use each coin as many times as necessary.
# If it is not possible to create the amount, then return -1.
def min_change(amount, coins):
  pass # todo


assert min_change(8, [1, 5, 4, 12]) == 2
assert min_change(13, [1, 9, 5, 14, 30]) == 5
assert min_change(23, [2, 5, 7]) == 4
assert min_change(102, [1, 5, 10, 25]) == 6
assert min_change(200, [1, 5, 10, 25]) == 8
assert min_change(271, [10, 8, 265, 24]) == -1