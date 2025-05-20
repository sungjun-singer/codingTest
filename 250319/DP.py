"""
이론 정리
DP. 이전의 값을 재활용 하는 알고리즘

DP에서 가장 중요한 것은 점화식

꼭 점화식을 세우고 코드를 짜야한다.

"""


"""
1. 아이디어
    - 점화식 : An = An-1 + An-2
    - N값 구하기 위해, for문 3부터 N까지의 값을 구해주기
    - 이전값, 이전이전값 더해서 10007로 나누어 저장
    
2. 시간복잡도
    - O(N)

3. 자료구조
    - DP값 저장하는 배열 : int[]
    - 최대값: 10006

"""

import sys
input = sys.stdin.readline

n = int(input())

arr = [1,2,3]


for i in range(3, n):
    arr.append((arr[i-1] + arr[i-2])%10007)

print(arr[n-1])
