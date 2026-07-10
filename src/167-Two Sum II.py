# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
class Solution:
	def twoSum(self, numbers:List[int], target:int) -> List[int]:
		left_index = 0
		right_index = len(numbers) - 1
		while left_index < right_index:
			index_sum = numbers[left_index] + numbers[right_index]
			if index_sum > target:
				right_index -= 1
			elif index_sum < target:
				left_index += 1
			else:
				return [left_index+1, right_index+1]