"""
1. 아이디어
    - 스택 두개를 만들고
    - 첫번째 스택 : 처음 배열 역으로 담아두는 스택
    - 두번째 스택 : 배열에서 pop한 값 넣어두는 스택
    - 반복문을 돌면서 한번 pop하고 그것을 변수에 넣어둠
    - 그리고 그거보다 큰 수가 나올때까지 첫번째 스택에서 pop하며 두번째 스택에 push
    - 큰 수가 나온다면 결과 배열에 값 저장해두고 첫번째 스택이 다 빌 때까지 안나온다면 -1저장
    - 그리고 두번째 스택에 있는 값들 다 pop해서 첫번째 스택에 다시 넣음.
2. 시간복잡도
    - 입력 뒤에서부터 첫번째 스택 담는 것 : O(n) -> 1,000,000
    - 반복문 돌면서 pop하고 push하고 배열에 저장하는 것 : O(2*n) -> 2,000,000
    - 배열 출력하는 것 : O(n) -> 1,000,000
    - 총 4,000,000 정도
3. 자료구조
    - 스택에 사용할 배열 2개(first_stack, second_stack)
    - 결과값 저장에 사용할 배열 1개(res)
    - 첫번째 스택 pop한 값(first_pop)
    - 하면서 변수 생성하자

"""

"""

import sys
input = sys.stdin.readline

n = int(input())
# 스택에 반대로 입력
first_stack = list(map(int, input().strip().split()))
first_stack.reverse()

second_stack = []
res = []

for i in range(1, n+1): # 이중
    # 비교할 첫번째 결과값
    first_pop = first_stack.pop()

    while len(first_stack): # 반복문
        # 클 경우 결과에 넣고 탈출
        if first_pop < first_stack[-1]:
            res.append(first_stack[-1])
            break
        # 작을 경우 두번째 스택에 넣기
        else:
            second_stack.append(first_stack.pop())

    # 만약에 끝까지 못찾았다면 -1 추가
    if len(res) is not i:
        res.append(-1)

    # 큰 값을 찾기 위해 뺐던 값들
    while len(second_stack):
        first_stack.append(second_stack.pop())

# 결과 출력
print(" ".join(map(str, res)))
"""

"""
len() 함수의 시간복잡도는 O(1)이다.
reverse() 도 inplace 함수 : 내부에서 다 동작함. 반환값 None
숫자 배열을 문자열로 변환하여 한칸씩 띄워서 출력하려면 " ".join(map(str, arr))를 사용하고,
문자열 배열을 문자열로 변환하여 한칸씩 띄워서 출력하는 건 " ".join(arr) 이다.
"""


import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
NGE = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i]
    stack.append(i)
print(*NGE)






