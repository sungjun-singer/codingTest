# import time
#
# str1 = input()
#
# stack = []
# razor = []
# pipe = []
#
# start_time = time.time()
#
# # 100,000번
# for idx, char in enumerate(str1):
#     if char == "(":
#         stack.append((idx*2, char))
#     else:
#         if idx*2 - stack[-1][0] == 2:
#             stack.pop()
#             razor.append(idx*2 - 1)
#         else:
#             pipe.append((stack.pop()[0], idx*2))
#
# pipe.sort()
# res = len(pipe)
#
#
# for x in razor:
#     for y in pipe:
#         (a,b) = y
#         if x < a:
#             break
#         if x >= a and x <= b:
#             res += 1
#
# print(res)
#


