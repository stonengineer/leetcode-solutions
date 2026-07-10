# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/description/
class Solution:
	def trap(self, height: List[int]) -> int:
		l_index, r_index = 0, len(height) - 1
		l_max, r_max = height[l_index], height[r_index]
		collected = 0

		while l_index < r_index:
			if l_max < r_max:
				collected += min(l_max, r_max) - height[l_index]
				l_index += 1
				if l_max < height[l_index]:
					l_max = height[l_index]
			else:
				collected += min(l_max, r_max) - height[r_index]
				r_index -= 1
				if r_max < height[r_index]:
					r_max = height[r_index]

		return collected