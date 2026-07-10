# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/description/
from collections import deque
class Solution:
	def minEatingSpeed(self, piles: List[int], h: int) -> int:
		def canFinish(k):
			hours_to_finish = 0
			pile_queue = deque(piles)
			while pile_queue:
				hours_to_finish += math.ceil(pile_queue.pop() / k)
			return hours_to_finish <= h

		smallest_result = -1
		l, r = 0, max(piles)
		while l <= r:
			mid = (l + r) // 2
			if canFinish(mid+1):
				smallest_result = mid+1
				r = mid - 1
			else:
				l = mid + 1

		return smallest_result