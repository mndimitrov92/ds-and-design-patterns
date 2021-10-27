from queue import deque

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None



# Build the tree
#		a
#    b     c
#  d   e     f
# depth first  - > a, b, d, e, c, f
# breadth first -> a, b, c, d, e ,f
root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.right = Node('f')



def depth_first_iter(root_elem):
	"""
	Depth first traversal on a binary tree using iteration
	Time Complexity : O(n)
	Space Complexity : O(n)
	"""
	result = []
	# For empty trees
	if root_elem is None:
		return result
	
	stack = [root_elem]
	while stack:
		# Capture the current element and add it to the result
		current = stack.pop()
		result.append(current.value)
		
		# if the current element has a left/right child, add it to the stack for checking
		if current.right:
			stack.append(current.right) 
		if current.left:
			stack.append(current.left)
	return result


def depth_first_recurse(root_elem):
	"""
	Depth first traversal on a binary tree using recursion
	"""
	if root_elem is None:
		return []
	left_elements = depth_first_recurse(root_elem.left)
	right_elements = depth_first_recurse(root_elem.right)
	return [root_elem.value, *left_elements, *right_elements]


assert depth_first_iter(root) == ['a', 'b', 'd', 'e', 'c', 'f']
assert depth_first_recurse(root) == ['a', 'b', 'd', 'e', 'c', 'f']
# =====================================================================

def breadth_first_iter(root_elem):
	"""
	Breadth first traversal on a binary tree (iterative solution)
	Time Complexity : O(n)
	Space Complexity : O(n)
	"""
	# Guard agains an empty tree
	result = []
	if root_elem is None:
		return result
	queue = deque([root_elem])
	while queue:
		current = queue.popleft()
		result.append(current.value)
		if current.left:
			queue.append(current.left)
		if current.right:
			queue.append(current.right)
	return result

assert breadth_first_iter(root) == ['a', 'b', 'c', 'd', 'e', 'f']


# Search if a target is in the tree
def search_in_tree(root_elem, target):
	"""
	Search algorithm for a target in a binary tree.
	Time Complexity : O(n)
	Space Complexity : O(n)
	"""
	# Guard agains an empty tree
	if root_elem is None:
		return False
	queue = deque([root_elem])
	while queue:
		current = queue.popleft()
		if current.value == target:
			return True
		if current.left:
			queue.append(current.left)
		if current.right:
			queue.append(current.right)
	return False


def search_in_tree_recurse(root_elem, target):
	"""
	Search algorithm for a target in a binary tree.
	Time Complexity : O(n)
	Space Complexity : O(n)
	"""
	# Guard agains an empty tree
	if root_elem is None:
		return False
	if root_elem.value == target:
		return True
	return search_in_tree_recurse(root_elem.left, target) or search_in_tree_recurse(root_elem.right, target)


assert search_in_tree(root, 'e') == True
assert search_in_tree(root, 'k') == False
assert search_in_tree_recurse(root, 'e') == True
assert search_in_tree_recurse(root, 'k') == False


# Build the tree
#		5
#    11     3
#  4   15      12

root2 = Node(5)
root2.left = Node(11)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)
root2.right.right = Node(12)



def sum_of_tree(root_elem):
	"""
	Return the sum of all elements in a binary tree.
	Recursive solution is depth first
	"""
	if root_elem is None:
		return 0
	return root_elem.value + sum_of_tree(root_elem.left) + sum_of_tree(root_elem.right)

assert sum_of_tree(root2) == 40


def min_value(root_elem):
	"""
	Returns the min value in a binary tree. 
	"""
	min_val = root_elem.value
	stack = [root_elem]
	while stack:
		# Capture the current element and add it to the result
		current = stack.pop()
		if current.value < min_val:
			min_val = current.value
		# if the current element has a left/right child, add it to the stack for checking
		if current.right:
			stack.append(current.right)
		if current.left:
			stack.append(current.left)
	return min_val

def min_value_rec(root_elem):
	if root_elem is None:
		return 999999
	left_min = min_value_rec(root_elem.left)
	right_min = min_value_rec(root_elem.right)
	return min(root_elem.value, left_min, right_min)

assert min_value(root2) == 3
assert min_value_rec(root2) == 3


def max_path_sum(root_elem):
	"""
	Return the maximum path sum of a binary tree.
	"""
	if root_elem is None:
		return 0
	if root_elem.left is None and root_elem.right is None:
		return root_elem.value
	max_child = max(max_path_sum(root_elem.left),max_path_sum(root_elem.left))
	return root_elem.value + max_child

assert max_path_sum(root2) == 20