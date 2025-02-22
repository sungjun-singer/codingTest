"""
주어진 수에서 64를 빼서 음수가 나오면 비트마스킹 연산을 통해 32로
주어진 수에서 32를 빼서 양수가 나오면 비트마스킹 연산을 통해 16으로

주어진 수가 0이 될때까지 빼는 것을 반복하면 될 듯


"""

n = int(input())
stick = 64
cnt = 0

while n != 0:
    if n  < stick:
        stick = stick >> 1
    else:
        n = n - stick
        stick = stick >> 1
        cnt += 1

print(cnt)

