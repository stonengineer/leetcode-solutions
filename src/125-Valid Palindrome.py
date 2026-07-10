# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/
import re
class Solution:
	def isPalindrome(self, s:str) -> bool:
		s_cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
		s_len = len(s_cleaned)
		if s_len == 0:
			return True
		s_left = s_cleaned[0:math.floor(s_len/2)]
		s_right = s_cleaned[math.ceil(s_len/2):s_len][::-1]
		return s_left == s_right