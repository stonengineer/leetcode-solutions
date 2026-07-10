# 695. Max Area of Island
# https://leetcode.com/problems/max-area-of-island/description/
from collections import deque
class Solution:
	def maxAreaOfIsland(self, grid:List[List[int]]) -> int:
		# helper vars
		max_island_area = 0
		island_queue = deque()
		traversed = set()
		grid_height = len(grid)
		grid_width = len(grid[0])

		# algorithm
		for y in range(grid_height):
			for x in range(grid_width):
				curr_pos = (y,x)
				if grid[y][x] == 1 and curr_pos not in traversed:
					island_queue.append(curr_pos)
					traversed.add(curr_pos)
					island_area = 0
					while island_queue:
						# extract position information
						queue_pos = island_queue.popleft()
						pos_y = queue_pos[0]
						pos_x = queue_pos[1]

						# increment island size
						island_area += 1

						# search for land in cardinal directions
						for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
							ny, nx = pos_y + dy, pos_x + dx
							if 0 <= ny < grid_height and 0 <= nx < grid_width:
								if grid[ny][nx] == 1 and (ny,nx) not in traversed:
									traversed.add((ny,nx))
									island_queue.append((ny,nx))

					# write back island area (sum of squares)
					max_island_area = max(max_island_area, island_area)

		# return result
		return max_island_area