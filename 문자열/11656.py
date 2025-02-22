"""
1. 아이디어
    - 입력이 주어지면 접미사들을 배열로 다 저장한다.
    - 배열 정렬하고 하나씩 출력한다.
2. 시간복잡도
    - 입력 1000 O(n) -> 1000
    - 정렬 1000 O(nlogn) -> 1000 * 10 -> 10000
3. 자료구조
    - String [] arr
"""

# import sys
# input = sys.stdin.readline
#
# S = input()
# arr = []
#
# for i in range(len(S)):
#     arr.append(S[i:len(S)-1])
#
# arr.pop()
#
# arr.sort()
#
# for x in arr:
#     print(x)

import random
import time

a = list(range(1000))

random.shuffle(a)
sorted(a)

print(a)


"""
이번 문제를 통해 공부한 것
정렬 알고리즘 sort vs sorted
sort는 inplace 함수라 반환 값이 없고 배열 자체를 바꿔버리는 함수이다.
예를 들어, arr = arr.sort() 를 한다면 None이 반환된다.
sorted는 반환 값이 있는 함수이다.
따라서 sorted(arr) 하면 정렬이 안되고
arr = sorted(arr) 해야 반환값으로 정렬된 배열을 넘겨준다.
"""