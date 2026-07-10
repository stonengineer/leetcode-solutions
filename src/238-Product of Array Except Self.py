# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/
class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		lenNums = len(nums)
		result = [1] * lenNums
		leftMults = 1
		for i in range(1, lenNums, 1):
			leftMults *= nums[i-1]
			result[i] = leftMults
		rightMults = 1
		for i in range(lenNums-2, -1, -1):
			rightMults *= nums[i+1]
			result[i] *= rightMults
		return result