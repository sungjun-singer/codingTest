"""
1. 아이디어
    - 입력을 받고 람다함수를 사용해서 국어, 수학, 영어, 이름 순서대로 정렬하고 출력한다.
2. 시간복잡도
    - sort의 시간 복잡도 O(nlogn) key function의 시간복잡도는 연산이지만 상수계수 수준이라 O(1)
    - 전체 시간복잡도 O(nlogn)
3. 자료구조
    - 튜플 배열 : [(),()]
"""

import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    data = input()
    [name, kor, math, eng] = data.split(" ")
    arr.append((name, int(kor), int(math), int(eng)))

arr = sorted(arr, key=lambda x : (-x[1], x[2], -x[3], x[0]))
for x in arr:
    print(x[0])


"""
이 문제를 통해 배운 것
- lambda : 런타임에 생성해서 사용할 수 있는 '익명 함수'
- arr = sorted(arr, key=lambda x : (-x[1], x[2])) 등으로 사용된다.
- 1순위, 2순위, 3순위 정렬에 많이 쓰이고 기본 정렬은 오름차순 정렬이고 -를 사용한다면 내림차순 정렬이 된다.
"""