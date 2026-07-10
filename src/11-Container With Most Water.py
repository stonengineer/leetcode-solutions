# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/
class Solution:
	def maxArea(self, height:List[int]) -> int:
		# define helper vars
		l_index = 0
		r_index = len(height)-1
		max_area = 0

		# iteration loop
		while l_index < r_index:
			curr_length = r_index - l_index
			if height[l_index] > height[r_index]:
				curr_area = height[r_index] * curr_length
				r_index -= 1
			else:
				curr_area = height[l_index] * curr_length
				l_index += 1
			if curr_area > max_area:
				max_area = curr_area

		# return result
		return max_area