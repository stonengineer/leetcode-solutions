# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/description/
class Solution:
	def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
		# Monotonic stack
		# define stack as list for indexed sorting
		if not temperatures:
			return []

		temp_stack = []
		n_temps = len(temperatures)
		answer = [0] * n_temps

		for index, temp in enumerate(temperatures):
			while temp_stack and temperatures[temp_stack[-1]] < temp:
				p_index = temp_stack.pop()
				answer[p_index] = index - p_index
			temp_stack.append(index)

		return answer