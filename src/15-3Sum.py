# 15. 3Sum
# https://leetcode.com/problems/3sum/description/
class Solution:
	def threeSum(self, nums:List[int]) -> List[List[int]]:
		solutions = []
		sorted_nums = sorted(nums)
		for index, num in enumerate(sorted_nums):
			if index == 0 or sorted_nums[index] != sorted_nums[index-1]:
				l_index = index+1
				r_index = len(sorted_nums)-1
				target = -1 * num
				while l_index < r_index:
					curr_sum = sorted_nums[l_index] + sorted_nums[r_index]
					if curr_sum > target:
						r_index -= 1
					elif curr_sum < target:
						l_index += 1
					else:
						solutions.append([num, sorted_nums[l_index], sorted_nums[r_index]])
						l_match_value = sorted_nums[l_index]
						r_match_value = sorted_nums[r_index]
						while l_index < len(sorted_nums)-1 and sorted_nums[l_index] == l_match_value:
							l_index += 1
						while r_index >= 0 and sorted_nums[r_index] == r_match_value:
							r_index -= 1
		return solutions