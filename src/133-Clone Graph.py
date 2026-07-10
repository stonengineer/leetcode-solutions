# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/description/
class Node:
	def __init__(self, val = 0, neighbors = None):
		self.val = val
		self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
from collections import deque
class Solution:
	def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
		# handle edge case
		if node is None:
			return None

		# build internal node tracker
		traversed_nodes = {}

		# recursive clone algorithm
		return self.cloneNode(node, traversed_nodes)

	def cloneNode(self, node: Optional['Node'], traversed_nodes: dict) -> Optional['Node']:
		curr_node = Node(node.val, [])
		traversed_nodes[curr_node.val] = curr_node
		for neighbor in node.neighbors:
			if neighbor.val in traversed_nodes:
				curr_node.neighbors.append(traversed_nodes.get(neighbor.val))
			else:
				curr_node.neighbors.append(self.cloneNode(neighbor, traversed_nodes))
		return curr_node