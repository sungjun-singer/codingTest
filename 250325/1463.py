"""
1. 아이디어
    - 1로 만들기이다.
    - 이것도 아까 문제처럼 그냥 1에서부터 시작해가지고
    - 1더하고 2곱하고 3곱하고를 다한다음에
    - 가장 작은 숫자를 배열에 저장해두면 된다.
2, 시간복잡도
    - O(n) 배열 한번 순회하기 때문에 1,000,000 아래
3. 자료구조
    - 연산 횟수 저장 배열 -> int []
"""

n = int(input())

arr = [0] * (n+1)

for i in range(2, n+1):
    if i % 6 == 0:
        arr[i] = min(arr[i//3], arr[i//2], arr[i-1]) + 1
    elif i%3 == 0:
        arr[i] = min(arr[i//3], arr[i-1]) + 1
    elif i%2 == 0:
        arr[i] = min(arr[i//2], arr[i-1]) + 1
    else:
        arr[i] = arr[i-1] +1

print(arr[n])