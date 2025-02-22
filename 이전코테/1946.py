import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    applicant_list = []
    for _ in range(n):
        t1, t2 = map(int, input().split())
        applicant_list.append((t1, t2))

    applicant_list.sort()

    cnt = 1
    min_interview_rank = applicant_list[0][1]

    for i in range(1, n):
        if applicant_list[i][1] < min_interview_rank:
            cnt += 1
            min_interview_rank = applicant_list[i][1]

    print(cnt)