# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/description/
from functools import lru_cache
class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		@lru_cache(maxsize=None)
		def best(index):
			if index == len(nums):
				return 0
			available_indeces = [i+index+1 for i, num in enumerate(nums[index+1:len(nums)]) if num > nums[index]]
			if available_indeces:
				return 1 + max(best(i) for i in available_indeces)
			else:
				return 1

		return max(best(i) for i in range(len(nums)))