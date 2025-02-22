"""
진짜 구현하기 전에 설계를 제대로 해놓고 하자
일단 구현부터 하다보면 무조건 막힌다
설계를 먼저 해놓고 그다음에 구현을 하자
이 문제에서 이분탐색을 사용할 경우
최악의 경우

상근이가 가지고 있는 숫자 카드가 1이 500,000개 있고
후보카드에도 1이 500,000개 있다면

500,000 X 500,000 이 나와버리니 2,500,000,000 이 나온다...
25억 ㄷㄷ 절대 안되지

그래서 이건 딕셔너리로 풀어야 한다.

"""


import sys
input = sys.stdin.readline

n = int(input())
sangen = sorted(list(map(int, input().split())))
m = int(input())
cards = list(map(int, input().split()))

dic1 = {}
for x in sangen:
    if x in dic1:
        dic1[x] += 1
    else:
        dic1[x] = 1

for element in cards:
    if element in dic1:
        print(dic1[element], end=' ')
    else:
        print(0, end=' ')

