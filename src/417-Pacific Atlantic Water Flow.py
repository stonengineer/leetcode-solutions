# 417. Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
from collections import deque
class Solution:
	def pacificAtlantic(self, heights:List[List[int]]) -> List[List[int]]:
		# handle edge case
		if not heights or not heights[0]:
			return []

		# array constants
		R_MIN = 0
		R_MAX = len(heights)
		C_MIN = 0
		C_MAX = len(heights[0])
		CARDINAL_DIRECTIONS = [(-1,0),(1,0),(0,-1),(0,1)]

		# helper storage vars
		pacific_queue = deque()
		atlantic_queue = deque()
		pacific_visited = set()
		atlantic_visited = set()

		# add edges to corresponding storage vars
		for r in range(R_MAX):
			# left border (pacific)
			pacific_queue.append((r, C_MIN))
			pacific_visited.add((r, C_MIN))
			# right border (atlantic)
			atlantic_queue.append((r, C_MAX-1))
			atlantic_visited.add((r, C_MAX-1))

		for c in range(C_MAX):
			# top border (pacific)
			pacific_queue.append((R_MIN, c))
			pacific_visited.add((R_MIN, c))
			# bottom border (atlantic)
			atlantic_queue.append((R_MAX-1, c))
			atlantic_visited.add((R_MAX-1, c))

		# reusable BFS worker
		def bfs(queue, visited_set):
			while queue:
				# get current position and height
				r, c = queue.popleft()
				height = heights[r][c]

				# search in all directions
				for dr,dc in CARDINAL_DIRECTIONS:
					# get step coordinates
					nr, nc = r + dr, c + dc

					# check boundary
					if R_MIN <= nr < R_MAX and C_MIN <= nc < C_MAX:
						# prevent dupes and verify height
						if (nr,nc) not in visited_set and heights[nr][nc] >= height:
							visited_set.add((nr,nc))
							queue.append((nr,nc))

		# execute workers for both oceans
		bfs(pacific_queue, pacific_visited)
		bfs(atlantic_queue, atlantic_visited)

		# return intersection of visited sets
		return list(pacific_visited & atlantic_visited)