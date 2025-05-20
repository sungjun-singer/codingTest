"""

1. 아이디어
    - opcode x rD rA (rB or C#) 의 구조로 16bit가 이루어져 있고
    - 각 opcode에 저장된 값이 있다. 그냥 다 번역해서 문자열로 리턴해주면 된다.
2. 시간복잡도
    -
3. 자료구조
    -
"""

import sys
input = sys.stdin.readline

n = int(input())

# 코드 딕셔너리 생성
opcode_set = {'ADD':"0000", "SUB": "0001", "MOV":"0010", "AND":"0011", "OR":"0100", "NOT" :"0101", "MULT":"0110", "LSFTL":"0111", "LSFTR":"1000", "ASFTR":"1001", "RL":"1010", "RR":"1011"}

# 어셈블리어 명령 저장
cmd = [input().strip() for _ in range(n)]


for x in cmd:
    res = ''
    # 명령어 구조분해할당
    opcode, rD, rA, rBorC = x.split()

    # 10진수를 2진수로 변환
    rD = format(int(rD), '03b')
    rA = format(int(rA), '03b')

    # opcode의 마지막 자리가 C일때, 12~15 자리 변환
    if opcode[-1] == "C":
        rBorC = format(int(rBorC), "04b")
    else:
        rBorC = format(int(rBorC), "03b") + '0'

    # opcode의 마지막 자리가 C일때, 0~5 자리 변환 후 결과에 더하기
    if opcode[-1] == "C":
        res += opcode_set[opcode[0:-1]] + "10"
    else:
        res += opcode_set[opcode] + "00"

    # 변환한 값들 다 더하기
    res += rD + rA + rBorC

    print(res)







