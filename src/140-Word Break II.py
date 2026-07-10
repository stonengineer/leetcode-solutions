# 140. Word Break II
# https://leetcode.com/problems/word-break-ii/description/?q=Word+Break
class Solution:
	def wordBreak(self, s:str, wordDict:List[str]) -> List[str]:
		memo = {}

		def buildPath(index):
			if index == len(s):
				return ['']
			if index in memo:
				return memo[index]
			path = []
			for word in wordDict:
				if s.startswith(word, index):
					for tail in buildPath(index + len(word)):
						path.append(word if tail == '' else word + ' ' + tail)
			memo[index] = path
			return path

		return buildPath(0)