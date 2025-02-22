# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# count = 0
# deq = deque([i for i in range(1, n+1)])
# cmd = list(map(int, input().split()))
#
# for target in cmd:
#     while True:
#         if deq[0] == target:
#             deq.popleft()
#             break
#         else:
#             if deq.index(target) < len(deq)/2:
#                 while deq[0] != target:
#                     deq.append(deq.popleft())
#                     count += 1
#             else:
#                 while deq[0] != target:
#                     deq.appendleft(deq.pop())
#                     count += 1
#
# print(count)

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().strip().split())
count = 0
deq = deque([i for i in range(1, n+1)])
cmd = list(map(int, input().split()))

print(*deq)