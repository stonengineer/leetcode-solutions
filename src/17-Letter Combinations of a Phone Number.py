# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		number_letters = {
			'2': ['a','b','c'],
			'3': ['d','e','f'],
			'4': ['g','h','i'],
			'5': ['j','k','l'],
			'6': ['m','n','o'],
			'7': ['p','q','r','s'],
			'8': ['t','u','v'],
			'9': ['w','x','y','z']
		}

		combinations = []

		def backtrack(index, current_path):
			if index == len(digits):
				combinations.append(current_path)
				return
			for letter in number_letters[digits[index]]:
				backtrack(index+1, current_path+letter)

		backtrack(0, '')

		return combinations