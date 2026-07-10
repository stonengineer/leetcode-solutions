# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/description/
class Solution:
	def climbStairs(self, n: int) -> int:
		if n <= 2:
			return n
		res_1 = 1
		res_2 = 2
		for i in range(2, n):
			tmp_res_2 = res_2
			res_2 = res_1 + res_2
			res_1 = tmp_res_2
		return res_2