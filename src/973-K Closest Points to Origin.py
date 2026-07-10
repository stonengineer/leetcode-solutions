# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/description/
import heapq
class Solution:
	def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
		def calcDistanceSquared(x,y):
			return (x*x) + (y*y)

		point_distances = list((calcDistanceSquared(x,y), [x,y]) for x,y in points)
		return [[point[0],point[1]] for distance, point in heapq.nsmallest(k, point_distances)]