# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
	def lengthOfLongestSubstring(self, s:str) -> int:
		char_index_map = {}
		l_index = 0
		max_length = 0

		for r_index, char in enumerate(s):
			if char in char_index_map and char_index_map[char] >= l_index:
				l_index = char_index_map[char] + 1
			char_index_map[char] = r_index
			max_length = max(max_length, r_index - l_index + 1)

		return max_length