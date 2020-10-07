# Python code to insert a node in AVL tree

# Generic tree node class
class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.height = 1

# AVL tree class which supports the
# Insert operation


class AVL_Tree(object):

	# Recursive function to insert key in
	# subtree rooted with node and returns
	# new root of subtree.
	def insert(self, root, key):

		# Step 1 - Perform normal BST
		if not root:
			return TreeNode(key)
		elif key < root.val:
			root.left = self.insert(root.left, key)
		else:
			root.right = self.insert(root.right, key)

		# Step 2 - Update the height of the
		# ancestor node
		root.height = 1 + max(self.getHeight(root.left),
						self.getHeight(root.right))

		# Step 3 - Get the balance factor
		balance = self.getBalance(root)

		# Step 4 - If the node is unbalanced,
		# then try out the 4 cases
		# Case 1 - Left Left
		if balance > 1 and key < root.left.val:
			return self.rightRotate(root)

		# Case 2 - Right Right
		if balance < -1 and key > root.right.val:
			return self.leftRotate(root)

		# Case 3 - Left Right
		if balance > 1 and key > root.left.val:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)

		# Case 4 - Right Left
		if balance < -1 and key < root.right.val:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)

		return root

	def leftRotate(self, z):

		y = z.right
		T2 = y.left

		# Perform rotation
		y.left = z
		z.right = T2

		# Update heights
		z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))

		# Return the new root
		return y

	def rightRotate(self, z):

		y = z.left
		T3 = y.right

		# Perform rotation
		y.right = z
		z.left = T3

		# Update heights
		z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))

		# Return the new root
		return y

	def getHeight(self, root):
		if not root:
			return 0

		return root.height

	def getBalance(self, root):
		if not root:
			return 0

		return self.getHeight(root.left) - self.getHeight(root.right)

	def preOrder(self, root):

		if not root:
			return

		print("{0} ".format(root.val), end="")
		self.preOrder(root.left)
		self.preOrder(root.right)
# # Driver program to test above function 
# myTree = AVL_Tree() 
# root = None

# root = myTree.insert(root, 10) 
# root = myTree.insert(root, 20) 
# root = myTree.insert(root, 30) 
# root = myTree.insert(root, 40) 
# root = myTree.insert(root, 50) 
# root = myTree.insert(root, 25) 
# print(myTree.getHeight(root))

# """The constructed AVL Tree would be 
# 			30 
# 		/ \ 
# 		20 40 
# 		/ \	 \ 
# 	10 25 50"""

# # Preorder Traversal 
# print("Preorder traversal of the", 
# 	"constructed AVL tree is") 
# myTree.preOrder(root) 
# print() 

# # This code is contributed by Ajitesh Pathak 

"""Python3 program to find value of the 
deepest node in a given binary tree"""

# A Binary Tree Node 
# Utility function to create a
# new tree node 
# class newNode: 

# 	# Constructor to create a newNode 
# 	def __init__(self, data): 
# 		self.data= data 
# 		self.left = None
# 		self.right = None
# 		self.visited = False

# # maxLevel : keeps track of maximum 
# # level seen so far. 
# # res : Value of deepest node so far. 
# # level : Level of root 
# def find(root, level, maxLevel, res):

# 	if (root != None):
# 		level += 1
# 		find(root.left, level, maxLevel, res) 

# 		# Update level and resue 
# 		if (level > maxLevel[0]):
		
# 			res[0] = root.data 
# 			maxLevel[0] = level 
		
# 		find(root.right, level, maxLevel, res) 
		
# # Returns value of deepest node 
# def deepestNode(root) :

# 	# Initialze result and max level 
# 	res = [-1] 
# 	maxLevel = [-1] 

# 	# Updates value "res" and "maxLevel" 
# 	# Note that res and maxLen are passed 
# 	# by reference. 
# 	find(root, 0, maxLevel, res) 
# 	return res[0]
						
# Driver Code
# if __name__ == '__main__':
# 	root = newNode(1) 
# 	root.left = newNode(2) 
# 	root.right = newNode(3) 
# 	root.left.left = newNode(4) 
# 	root.right.left = newNode(5) 
# 	root.right.right = newNode(6) 
# 	root.right.left.right = newNode(7) 
# 	root.right.right.right = newNode(8) 
# 	root.right.left.right.left = newNode(9) 
# 	print(deepestNode(root))

nodes = input().split(', ')

# This code is contributed by
# SHUBHAMSINGH10

