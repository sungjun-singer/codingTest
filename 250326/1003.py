"""
1. 아이디어
    - 피보나치 수열에서 0이랑 1의 호출 횟수를 구하는 문제
    - 그럼 그냥 함수 호출 횟수만 쓰면 되는거 아닌가
    - 이걸 DP로 할 수 있나?
    - (0횟수, 1횟수) 해서 배열에 저장해두고 출력하면 될라나
2. 시간복잡도
    -
3. 자료구조

"""


T = int(input())

arr = [[1,0], [0,1], [1,1]]

for _ in range(38):
    arr.append([0,0])


for i in range(3, 41):
    arr[i][0] = arr[i-1][0] + arr[i-2][0]
    arr[i][1] = arr[i-1][1] + arr[i-2][1]


for _ in range(T):

    n = int(input())

    zero = 0
    one = 0

    print(arr[n][0], end=' ')
    print(arr[n][1])


