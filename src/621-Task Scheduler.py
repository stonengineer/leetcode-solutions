# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/description/
import heapq
from collections import deque, Counter
class Solution:
	def leastInterval(self, tasks: List[str], n: int) -> int:
		# create max-heap for tasks with values
		max_heap = [-count for count in Counter(tasks).values()]
		heapq.heapify(max_heap)

		# store pairs of (rem, cd)
		cooldown_queue = deque()
		step_count = 0

		while max_heap or cooldown_queue:
			step_count += 1

			if max_heap:
				rem_count = heapq.heappop(max_heap) + 1
				if rem_count < 0:
					cooldown_queue.append((rem_count, step_count + n))

			if cooldown_queue and cooldown_queue[0][1] == step_count:
				ready_task_rem_count, _ = cooldown_queue.popleft()
				heapq.heappush(max_heap, ready_task_rem_count)

		return step_count