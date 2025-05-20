"""
1. 아이디어
    - 숫자와 몇진법을 사용했는지 주어진다. 이를 십진수로 바꿔야 한다.
    - 일의자리 * N^0 + 둘째자리 * N^1 + 셋째자리 * N^2
    - 주어진 숫자를 아스키 코드를 이용해서 숫자로 넣는다.
2. 시간복잡도
    - B진법 수의 개수 만약 B가 2라면 이진법 수의 길이는 30 -> 최대길이
    - 30번 연산하면 끝
3. 자료구조
    - 배열 : int []
"""

import sys
input = sys.stdin.readline

n, b = input().split()

arr = list(n)

# 일의 자리부터 시작하기 위함
arr.reverse()



res = 0

for i in range(len(arr)):
    if arr[i].isdigit():
        res += (int(b)**i) * int(arr[i])
    else:
        res += (int(b) ** i) * (ord(arr[i])-55)

print(res)


