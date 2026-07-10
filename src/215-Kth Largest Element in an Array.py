# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
import random
class Solution:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		# handle edge case
		if not nums:
			return None

		# pick a random pivot
		pivot = random.choice(nums)

		# split array into 3 chunks
		left = [num for num in nums if num < pivot]
		mid = [num for num in nums if num == pivot]
		right = [num for num in nums if num > pivot]

		# decide next step
		if k-1 < len(right):
			return self.findKthLargest(right, k)
		if k-1 < len(right) + len(mid):
			return pivot
		return self.findKthLargest(left, k - len(right) - len(mid))