# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
	def maxProfit(self, prices:List[int]) -> int:
		if len(prices) == 0:
			return 0
		min_price = prices[0]
		profit = 0
		for price in prices:
			if price < min_price:
				min_price = price
			else:
				curr_profit = price - min_price
				if curr_profit > profit:
					profit = curr_profit
		return profit