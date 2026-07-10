# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/
from collections import Counter
class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		# handle diff len strings
		if len(s) != len(t):
			return False

		# convert to counter objects
		s_counts = Counter(list(s))
		t_counts = Counter(list(t))

		# compare counters
		for s_key in s_counts.keys():
			if t_counts.get(s_key) is None:
				return False
			if s_counts[s_key] != t_counts[s_key]:
				return False
			del t_counts[s_key]

		# false if t_counts has any remaining keys
		if len(t_counts) > 0:
			return False

		# must be anagrams
		return True