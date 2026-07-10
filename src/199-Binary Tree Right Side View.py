# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/description/
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

from collections import defaultdict
class Solution:
	def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
		if not root:
			return []

		results = defaultdict(int)

		def dfs(node, depth):
			results[depth] = node.val
			if node.left:
				dfs(node.left, depth+1)
			if node.right:
				dfs(node.right, depth+1)

		dfs(root, 0)
		return list(results.values())