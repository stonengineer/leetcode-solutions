# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/
from collections import Counter
import heapq
class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		counts_by_num = []
		heapq.heapify(counts_by_num)
		for num, count in Counter(nums).items():
			heapq.heappush(counts_by_num, ((-1 * count), num))
		return [item[1] for item in heapq.nsmallest(k, counts_by_num)]