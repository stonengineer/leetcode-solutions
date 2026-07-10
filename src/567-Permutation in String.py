# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/description/
class Solution:
	def checkInclusion(self, s1:str, s2:str) -> bool:
		# edge case handling
		if len(s1) > len(s2):
			return False

		# define key windows
		s1_key = [0] * 26
		s2_key = [0] * 26

		# build s1 key and init s2 key
		for i in range(len(s1)):
			s1_key[ord(s1[i]) - ord('a')] += 1
			s2_key[ord(s2[i]) - ord('a')] += 1

		for i in range(len(s2) - len(s1)):
			if s1_key == s2_key:
				return True
			s2_key[ord(s2[i + len(s1)]) - ord('a')] += 1
			s2_key[ord(s2[i]) - ord('a')] -= 1

		return s1_key == s2_key