# 79. Word Search
# https://leetcode.com/problems/word-search/description/
class Solution:
	def exist(self, board: List[List[str]], word: str) -> bool:
		if not board or not word:
			return False

		DIRECTIONS = [(-1,0),(1,0),(0,-1),(0,1)]
		Y_MAX = len(board)
		X_MAX = len(board[0])

		def findWord(index, prevMoves, currPos):
			if index == len(word):
				return True
			y,x = currPos
			for move in DIRECTIONS:
				dy,dx = move
				ny,nx = y+dy, x+dx
				if (ny,nx) not in prevMoves and (0 <= ny < Y_MAX) and (0 <= nx < X_MAX) and board[ny][nx] == word[index]:
					valid_move = set([(ny,nx)])
					if findWord(index+1, prevMoves | valid_move, (ny,nx)):
						return True
			return False

		for y in range(Y_MAX):
			for x in range(X_MAX):
				if word[0] == board[y][x] and findWord(1, set([(y,x)]), (y,x)):
					return True

		return False