# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/description/
from functools import lru_cache
class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		@lru_cache(maxsize=None)
		def nextStep(pos):
			y,x = pos
			if y == m-1 and x == n-1:
				return 1
			if y >= m or x >= n:
				return 0

			down_paths = nextStep((y+1,x))
			right_paths = nextStep((y,x+1))

			return down_paths + right_paths

		return nextStep((0, 0))