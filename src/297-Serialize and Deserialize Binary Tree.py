# 297. Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
from collections import deque

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Codec:

	def serialize(self, root):
		"""Encodes a tree to a single string.
		
		:type root: TreeNode
		:rtype: str
		"""
		if not root:
			return '[]'
		collection = []
		node_queue = deque([root])
		while node_queue:
			curr_node = node_queue.popleft()
			if curr_node:
				collection.append(str(curr_node.val))
				node_queue.append(curr_node.left)
				node_queue.append(curr_node.right)
			else:
				collection.append('null')
		return '[' + ','.join(collection) + ']'

	def deserialize(self, data):
		"""Decodes your encoded data to tree.
		
		:type data: str
		:rtype: TreeNode
		"""
		if data == '[]':
			return None
		nodes = data[1:-1].split(',')
		root = TreeNode(int(nodes[0]))
		parent_nodes = deque([root])
		node_index = 1
		while parent_nodes and node_index < len(nodes):
			curr_parent = parent_nodes.popleft()
			if nodes[node_index] != 'null':
				left_child = TreeNode(int(nodes[node_index]))
				curr_parent.left = left_child
				parent_nodes.append(left_child)
			node_index += 1
			if node_index < len(nodes) and nodes[node_index] != 'null':
				right_child = TreeNode(int(nodes[node_index]))
				curr_parent.right = right_child
				parent_nodes.append(right_child)
			node_index += 1
		return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))