# 127. Word Ladder
# https://leetcode.com/problems/word-ladder/
from collections import deque
class Solution:
	def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
		word_set = set(wordList)

		if endWord not in word_set:
			return 0

		queue = deque([(beginWord, 1)])
		visited = {beginWord}

		while queue:
			word, length = queue.popleft()
			for i in range(len(word)):
				for alpha in 'abcdefghijklmnopqrstuvwxyz':
					next_word = word[:i] + alpha + word[i+1:]
					if next_word == endWord:
						return length + 1
					if next_word in word_set and next_word not in visited:
						visited.add(next_word)
						queue.append((next_word, length + 1))
		return 0