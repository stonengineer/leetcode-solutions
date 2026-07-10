# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def maxDepth(self, root: Optional[TreeNode]) -> int:
		# handle edge cases
		if root is None:
			return 0

		# define dfs helper
		def dfs(root, depth, end_depths):
			if root.left is None and root.right is None:
				end_depths.append(depth)
				return
			if root.left is not None:
				dfs(root.left, depth+1, end_depths)
			if root.right is not None:
				dfs(root.right, depth+1, end_depths)

		# call dfs with seed
		end_depths = []
		dfs(root, 1, end_depths)

		# return result
		return max(end_depths)