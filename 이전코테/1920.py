# # Set을 통한 중복제거를 통한 탐색
#
# # ============================================================
#
# # n = int(input())
# # arr = list(input().split())
# #
# # m = int(input())
# # arr2 = list(input().split())
# #
# # set1 = set(arr)
# #
# # for x in arr2:
# #     if x in set1:
# #         print(1)
# #     else:
# #         print(0)
#
# # ============================================================
#
# def binary_search(target, data):
#     start = 0
#     end = len(data) - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if data[mid] == target:
#             return 1
#         elif data[mid] > target:
#             end = mid -1
#         else:
#             start = mid + 1
#     return 0
#
# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
#
# m = int(input())
# arr2 = list(map(int, input().split()))
#
#
# for x in arr2:
#     if binary_search(x, arr):
#         print(1)
#     else:
#         print(0)
#
#
#
#
#
#
#
#

print(hash("apple"))
print(hash("apple"))
print(hash("bucket"))