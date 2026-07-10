# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/description/
from collections import deque
class Solution:
	def numIslands(self, grid:List[List[str]]) -> int:
		grid_height = len(grid)
		grid_width = len(grid[0])
		island_count = 0
		bfs_queue = deque()
		visited = set()
		for y in range(grid_height):
			for x in range(grid_width):
				if grid[y][x] == '1':
					curr_pos = (y,x)
					if curr_pos not in visited:
						island_count += 1
						bfs_queue.append(curr_pos)
						visited.add(curr_pos)
						while bfs_queue:
							coords = bfs_queue.popleft()
							visited.add(coords)
							coords_y = coords[0]
							coords_x = coords[1]
							north = '0' if coords_y-1 < 0 else grid[coords_y-1][coords_x]
							east = '0' if coords_x+1 >= grid_width else grid[coords_y][coords_x+1]
							south = '0' if coords_y+1 >= grid_height else grid[coords_y+1][coords_x]
							west = '0' if coords_x-1 < 0 else grid[coords_y][coords_x-1]
							if north == '1':
								north_coords = (coords_y-1, coords_x)
								if north_coords not in visited:
									visited.add(north_coords)
									bfs_queue.append(north_coords)
							if east == '1':
								east_coords = (coords_y, coords_x+1)
								if east_coords not in visited:
									visited.add(east_coords)
									bfs_queue.append(east_coords)
							if south == '1':
								south_coords = (coords_y+1, coords_x)
								if south_coords not in visited:
									visited.add(south_coords)
									bfs_queue.append(south_coords)
							if west == '1':
								west_coords = (coords_y, coords_x-1)
								if west_coords not in visited:
									visited.add(west_coords)
									bfs_queue.append(west_coords)
		return island_count