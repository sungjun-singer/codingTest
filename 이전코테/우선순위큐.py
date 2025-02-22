# from queue import PriorityQueue
#
# q = PriorityQueue()
# q1 = PriorityQueue(maxsize=10)
#
# q.put(4)
# q.put(3)
# q.put(1)
#
# q1.put((1, "apple"))
#
# print(q.get())
# print(q1.get()[1])

import heapq

hq = []

heapq.heappush(hq, 1)
heapq.heappush(hq, 2)
heapq.heappush(hq, 3)
heapq.heappush(hq, 5)
heapq.heappush(hq, 4)

print(hq)