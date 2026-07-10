# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/description/
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		# handle edge cases
		if root is None or (root.left is None and root.right is None):
			return root

		# dfs helper
		def dfs(root):
			new_right = None
			new_left = None
			if root.left is not None:
				new_right = dfs(root.left)
			if root.right is not None:
				new_left = dfs(root.right)
			root.right = new_right
			root.left = new_left
			return root

		# run dfs and track results
		root = dfs(root)

		# return root
		return root