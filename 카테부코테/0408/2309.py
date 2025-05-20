"""
1. 아이디어
    - 모든 난쟁이의 키를 다 받고 100이 되는 걸 출력하면 된다.
    - 다 더한다음에 2명 빼서 100이 나오면 컷
    -

2. 시간복잡도

3. 자료구조

"""

import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]

arr.sort()

res = sum(arr)
