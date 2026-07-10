# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/
from collections import deque
class Solution:
	def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
		# Kahn's BFS #
		"""
		1. Build lookup adjacency dict and in_degree list
			a. dict[prereq] = [courses]
			b. in_degree[course] = count of prereqs
		2. Build queue seeded with any nodes that have no prereqs
		3. Build empty result container
		4. While queue has values:
			a. Popleft on queue, append value to result container
			b. Iteracte adjacent keys and decrement the in_degree for that key
			c. If a key's in_degree is now 0, append it to the queue
		5. Cycle/contradiction check: if len(result) != len(in_degree), return failure value
		"""
		adjacent_courses = {i:[] for i in range(numCourses)}
		in_degree = [0] * numCourses
		for course, prereq in prerequisites:
			adjacent_courses[prereq].append(course)
			in_degree[course] += 1

		course_queue = deque(c for c in range(numCourses) if in_degree[c] == 0)

		course_order = []
		while course_queue:
			curr_course = course_queue.popleft()
			course_order.append(curr_course)
			for course in adjacent_courses[curr_course]:
				in_degree[course] -= 1
				if in_degree[course] == 0:
					course_queue.append(course)

		return course_order if len(course_order) == numCourses else []