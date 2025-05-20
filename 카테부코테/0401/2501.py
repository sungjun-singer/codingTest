"""
1. 아이디어
    - 약수를 구하는 문제인데 제곱근까지만 반복문 돌리고 약수를 배열에 추가하고
    - 약수로 N을 나눠서 나온 값을 배열에 추가한다.
    - 배열의 길이보다 큰 인덱스를 뽑으라고 할 경우에는 0을 출력하고
    - 아니라면 그냥 출력
2. 시간복잡도
    - 10000 이하니까 사실 그냥 다 돌려도 될듯한데 제곱근으로 하게 되면 100 * 2
3. 자료구조
    - 정수 입력 변수 : n, k
    - 약수 저장 배열 : int []

"""
import math
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

num = math.floor(math.sqrt(n)) + 1

res = []

for i in range(1, num):
    if n%i == 0:
        # 만약 같은 약수가 나온다면 하나만 넣기
        if (i == n//i):
            res.append(i)
        else:
            # 발견한 약수와
            res.append(i)
            # 약수의 쌍을 배열에 넣는다.
            res.append(n // i)

res.sort()

if len(res) < k:
    print(0)
else:
    print(res[k-1])


