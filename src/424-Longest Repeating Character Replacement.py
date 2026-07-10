# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
class Solution:
	def characterReplacement(self, s:str, k:int) -> int:
		char_counts = {}
		l_index = 0
		max_freq = 0
		max_length = 0

		for r_index in range(len(s)):
			# update dict with curr char
			curr_char = s[r_index]
			char_counts[curr_char] = char_counts.get(curr_char, 0) + 1

			# update highest frequency character
			max_freq = max(max_freq, char_counts[curr_char])

			# determine window size
			window_size = r_index - l_index + 1

			# if window size - max_freq > k, we need to shift right
			if window_size - max_freq > k:
				char_counts[s[l_index]] -= 1
				l_index += 1

			# determine biggest length of window, or retain previous biggest
			max_length = max(max_length, r_index - l_index + 1)

		return max_length