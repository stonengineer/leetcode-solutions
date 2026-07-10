# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/
from collections import defaultdict
class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		anagramsByKey = defaultdict(list)
		for str in strs:
			strId = self.computeAnagramIdentifier(str)
			anagramsByKey[strId].append(str)
		return list(anagramsByKey.values())

	def computeAnagramIdentifier(self, val: str) -> str:
		sortedCharList = list(val)
		sortedCharList.sort()
		return "".join(sortedCharList)