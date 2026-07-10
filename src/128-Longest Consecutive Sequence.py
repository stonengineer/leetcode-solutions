# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/description/
class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		nums_dict = dict.fromkeys(nums, True) # build O(1) access for numbers in list
		longest = 0
		for num in nums:
			if not nums_dict:
				return longest
			if nums_dict.get(num) is not None and nums_dict.get(num-1) is None:
				sequence_length = 0
				curr_num = num
				while nums_dict.get(curr_num) is not None:
					del nums_dict[curr_num]
					curr_num += 1
					sequence_length += 1
				if sequence_length > longest:
					longest = sequence_length
		return longest