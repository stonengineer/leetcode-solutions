# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/description/
from collections import Counter, defaultdict
class Solution:
	def minWindow(self, s: str, t: str) -> str:
		# edge cases
		if not s or not t or len(s) < len(t):
			return ""
		if len(s) == 1:
			return s if s == t else ""

		# helper vars
		l_index = 0
		t_counts = Counter(t)
		need = len(t_counts)
		have = 0
		window_counts = defaultdict(int)
		result = (float('inf'),'')

		for r_index in range(len(s)):
			char = s[r_index]
			window_counts[char] += 1
			if char in t_counts and window_counts[char] == t_counts[char]:
				have += 1
			while have == need:
				curr_len = r_index - l_index + 1
				if curr_len < result[0]:
					result = (curr_len, s[l_index:r_index+1])
				left_char = s[l_index]
				window_counts[left_char] -= 1
				if left_char in t_counts and window_counts[left_char] < t_counts[left_char]:
					have -= 1
				l_index += 1

		return result[1]
