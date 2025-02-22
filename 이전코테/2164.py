# from collections import deque
#
# def solution(n):
#     if n == 1:
#         return 1
#     q = deque()
#
#     for i in range(n):
#         q.append(n-i)
#
#     while q:
#         q.pop()
#
#         if len(q) == 1:
#             return q.pop()
#         x = q.pop()
#         q.appendleft(x)
#
# n = int(input())
# print(solution(n))
#
#
#

from queue import Queue

def solution(n):
    if n == 1:
        return 1
    q = Queue()

    for i in range(1, n+1):
        q.put(i)

    while q:
        q.get()

        if q.qsize() == 1:
            return q.get()
        x = q.get()
        q.put(x)

n = int(input())
print(solution(n))
