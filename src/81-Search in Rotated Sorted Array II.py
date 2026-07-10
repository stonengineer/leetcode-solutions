# 81. Search in Rotated Sorted Array II
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
class Solution:
	def search(self, nums: List[int], target: int) -> bool:
		# binary search with sorted half -- maybe
		l_index = 0
		r_index = len(nums)-1

		while l_index <= r_index:
			m_index = (r_index + l_index) // 2
			if nums[l_index] == target or nums[r_index] == target or nums[m_index] == target:
				return True

			if nums[l_index] == nums[m_index] == nums[r_index]:
				l_index += 1
				r_index -= 1
			elif nums[l_index] <= nums[m_index]:
				if nums[l_index] <= target < nums[m_index]:
					r_index = m_index - 1
				else:
					l_index = m_index + 1
			else:
				if nums[m_index] < target <= nums[r_index]:
					l_index = m_index + 1
				else:
					r_index = m_index - 1

		return False