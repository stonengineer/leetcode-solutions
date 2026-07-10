# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

from collections import deque
class Solution:
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		if not root or (not root.left and not root.right):
			return root

		def recurseTree(node):
			if not node or node.val == p.val or node.val == q.val:
				return node
			left_result = recurseTree(node.left)
			right_result = recurseTree(node.right)
			if left_result and right_result:
				return node
			return left_result if left_result else right_result

		return recurseTree(root)