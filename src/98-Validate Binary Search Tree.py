# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/description/
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

from collections import deque
class Solution:
	def isValidBST(self, root: Optional[TreeNode]) -> bool:
		if root is None:
			return False

		bfs_queue = deque([(root, float('-inf'), float('inf'))])

		while bfs_queue:
			curr_node, low, high = bfs_queue.popleft()

			if not (low < curr_node.val < high):
				return False
			if curr_node.left:
				bfs_queue.append((curr_node.left, low, curr_node.val))
			if curr_node.right:
				bfs_queue.append((curr_node.right, curr_node.val, high))

		return True