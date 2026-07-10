# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/description/
from collections import defaultdict, deque
class Solution:
	def canFinish(self, numCourses:int, prerequisites:List[List[int]]) -> bool:
		return self.dfsCanFinish(numCourses, prerequisites)
		# return self.bfsCanFinish(numCourses, prerequisites)

	def dfsCanFinish(self, numCourses:int, prerequisites:List[List[int]]) -> bool:
		graph = defaultdict(list)
		for course, prereq in prerequisites:
			graph[course].append(prereq)

		# 0 = unvisited, 1 = visiting, 2 = processed
		state = [0] * numCourses

		def dfs(course):
			if state[course] == 1: # cycle
				return False
			if state[course] == 2: #safe
				return True
			state[course] = 1
			for prereq in graph[course]:
				if not dfs(prereq):
					return False
			state[course] = 2
			return True

		for course in range(numCourses):
			if not dfs(course):
				return False

		return True

	def bfsCanFinish(self, numCourses:int, prerequisites:List[List[int]]) -> bool:
		graph = defaultdict(list)
		in_degree = [0] * numCourses

		for course, prereq in prerequisites:
			graph[prereq].append(course)
			in_degree[course] += 1

		# start on courses with no prereqs
		queue = deque([c for c in range(numCourses) if in_degree[c] == 0])
		completed = 0

		while queue:
			course = queue.popleft()
			completed += 1
			for next_course in graph[course]:
				in_degree[next_course] -= 1
				if in_degree[next_course] == 0:
					queue.append(next_course)

		return completed == numCourses