# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/
class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		tracked = {}
		for index, num in enumerate(nums):
			complement = target - num
			if complement in tracked:
				return [tracked[complement], index]
			tracked[num] = index