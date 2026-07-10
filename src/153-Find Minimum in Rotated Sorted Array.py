# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
import random
class Solution:
	def findMin(self, nums: List[int]) -> int:
		def binary_search(l, r):
			if l >= r:
				return nums[l]

			mid = l + ((r - l) // 2)
			if nums[mid] > nums[r]:
				return binary_search(mid+1, r)
			return binary_search(l, mid)

		return binary_search(0, len(nums)-1)