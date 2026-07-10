# 84. Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/
class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		max_rect = (0, -1, -1) # area, l_index, r_index

		def calcArea(l_index, r_index):
			if l_index == r_index:
				return
			minHeight = min(heights[l_index:r_index])
			area = (r_index - l_index) * minHeight
			if area > max_rect[0]:
				max_rect = (area, l_index, r_index)
			if heights[l_index] < heights[r_index]:
				calcArea(l_index+1, r_index)
			else:
				calcArea(l_index, r_index-1)

		calcArea(0, len(heights))

		return max_rect