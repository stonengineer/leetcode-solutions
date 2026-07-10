# 139. Word Break
# https://leetcode.com/problems/word-break/description/
from functools import lru_cache
class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		@lru_cache(maxsize=None)
		def canBreak(index):
			if index == len(s):
				return True
			next_word_options = [word for word in wordDict if s[index:].startswith(word)]
			if next_word_options:
				return any(canBreak(index+len(word)) for word in next_word_options)
			else:
				return False

		return canBreak(0)