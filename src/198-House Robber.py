# 198. House Robber
# https://leetcode.com/problems/house-robber/description/
from functools import lru_cache
class Solution:
	def rob(self, nums: List[int]) -> int:
		@lru_cache(maxsize=None)
		def best(index):
			if index >= len(nums):
				return 0
			return max(nums[index] + best(index+2), best(index+1))

		return best(0)