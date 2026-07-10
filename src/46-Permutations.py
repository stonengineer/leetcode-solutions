# 46. Permutations
# https://leetcode.com/problems/permutations/description/
class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		permutations = []

		def backtrack(permutation, available_indeces):
			if len(available_indeces) == 0: # base_case
				permutations.append(permutation[:])
				return
			for i in available_indeces:
				rem_indeces = set([i])
				permutation.append(nums[i])
				backtrack(permutation, available_indeces - rem_indeces)
				permutation.pop()

		for i in range(len(nums)):
			backtrack([nums[i]], set([n for n in range(len(nums)) if n != i]))

		return permutations