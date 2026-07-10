# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution:
	def search(self, nums: List[int], target: int) -> int:
		l, r = 0, len(nums)-1
		while l <= r:
			mid = (l + r) // 2

			# we found it
			if nums[mid] == target:
				return mid

			# is left half sorted
			if nums[l] <= nums[mid]:

				# does target lie within left?
				if nums[l] <= target < nums[mid]:
					r = mid - 1

				# target must lie within right
				else:
					l = mid + 1

			# right half sorted
			else:

				# does target lie within right?
				if nums[mid] < target <= nums[r]:
					l = mid + 1

				# target must lie within left
				else:
					r = mid - 1

		# target not found
		return -1