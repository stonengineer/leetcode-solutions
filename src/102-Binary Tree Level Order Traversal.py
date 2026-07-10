# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

from collections import deque,defaultdict
class Solution:
	def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		if root is None:
			return []

		bfs_queue = deque()
		bfs_queue.append(root)
		results = defaultdict(list)

		def depthAwareDFS(node, depth):
			results[depth].append(node.val)
			if node.left is not None:
				depthAwareDFS(node.left, depth+1)
			if node.right is not None:
				depthAwareDFS(node.right, depth+1)

		depthAwareDFS(root, 0)

		return list(results.values())