# 322. Coin Change
# https://leetcode.com/problems/coin-change/description/
from functools import lru_cache
class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		@lru_cache(maxsize=None)
		def spendCoin(rem_amount):
			if rem_amount == 0:
				return 0
			else:
				available_coins = [coin for coin in coins if coin <= rem_amount]
				if available_coins: 
					return 1 + min(spendCoin(rem_amount - coin) for coin in available_coins)
				else:
					return float('inf')

		total_coins = spendCoin(amount)
		if total_coins == float('inf'):
			return -1
		return total_coins