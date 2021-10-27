# Write a function, linked_list_values, that takes in the head of a linked list as an argument.
# The function should return a list containing all values of the nodes in the linked list.
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")

# a -> b -> c -> d
a.next = b
b.next = c
c.next = d
d.next = e

def linked_list_values(head):
	"""
	Collect all the values of a linked list
	"""
	result = []
	current = head
	while current is not None:
		result.append(current.val)
		current = current.next
	return result


assert linked_list_values(a) == ['a', 'b', 'c', 'd', 'e']


def get_middle_node(head):
	"""
	Finds the middle node in a linked list
	"""
	slow_p = head
	fast_p = head
	while fast_p.next and fast_p.next.next:
		fast_p = fast_p.next.next
		slow_p = slow_p.next
	print(slow_p.val)
	return slow_p.val

assert get_middle_node(a) == 'c'

# =====================================================================================
# Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument.
# The function should return the total sum of all values in the linked list.
a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

# 2 -> 8 -> 3 -> -1 -> 7
a.next = b
b.next = c
c.next = d
d.next = e


def sum_list(head):
	"""
	Calculates the sum of all items in a linked list
	"""
	total = 0
	current = head
	while current is not None:
		total += current.val
		current = current.next
	return total


def sum_list_rec(head):
	if head is None:
		return 0
	return head.val + sum_list_rec(head.next)


assert sum_list(a) == 19
assert sum_list_rec(a) == 19

# =====================================================================================
# Write a function, linked_list_find, that takes in the head of a linked list and a target value.
# The function should return a boolean indicating whether or not the linked list contains the target.
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

# a -> b -> c -> d
a.next = b
b.next = c
c.next = d

def linked_list_find(head, target):
	current = head
	while current is not None:
		if current.val == target:
			return True
		current = current.next
	return False

def linked_list_find_rec(head, target):
	if head is None:
		return False
	if head.val == target:
		return True
	return linked_list_find_rec(head.next, target)

assert linked_list_find(a, "c") == True
assert linked_list_find_rec(a, "c") == True

# =============================================================================
# Write a function, get_node_value, that takes in the head of a linked list and an index.
# The function should return the value of the linked list at the specified index.
# If there is no node at the given index, then return None.
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

# a -> b -> c -> d
a.next = b
b.next = c
c.next = d


def get_node_value(head, target):
	start = 0
	current = head
	while current is not None:
		if start == target:
			return current.val
		current = current.next
		start += 1


def get_node_value_rec(head, index):
  if head is None:
    return None
  if index == 0:
    return head.val
  return get_node_value(head.next, index - 1)

assert get_node_value(a, 2) == 'c'
assert get_node_value_rec(a, 2) == 'c'

# Write a function, reverse_list, that takes in the head of a linked list as an argument.
#The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

# a -> b -> c -> d -> e -> f
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f


def reverse_list(head):
	prev = None
	current = head
	while current is not None:
		next_item = current.next
		current.next = prev
		prev = current
		current = next_item
	return prev

reverse_list(a) # f -> e -> d -> c -> b -> a
print(f.next.val)


