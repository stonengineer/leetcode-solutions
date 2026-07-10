# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/description/
class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		combinations = []

		def backtrack(start_index, curr_combo, curr_sum):
			if curr_sum == target:
				combinations.append(curr_combo[:])
				return
			elif curr_sum > target:
				return
			for i in range(start_index, len(candidates)):
				curr_combo.append(candidates[i])
				backtrack(i, curr_combo, curr_sum + candidates[i])
				curr_combo.pop()

		for i in range(len(candidates)):
			backtrack(i, [candidates[i]], candidates[i])

		return combinations