import sys

T = int(sys.stdin.readline())
for t in range(T):
    n = int(sys.stdin.readline())
    score = []
    result = [0] * n
    cnt = 1
    for i in range(n):
        a, b = map(int, sys.stdin.readline().split())
        score.append([a, b])
    score.sort(key=lambda x:(x[0]))
    #i의 앞순위(i-1)의 면접순위가 자신보다 높으면(숫자가 작으면) i는 탈락
    #앞 순위들 중 본인보다 면접순위가 높은 사람이 한명이라도 있으면 i는 탈락
    mini = score[0][1]
    for i in range(1, n):
        if score[i][1] < mini:
            cnt += 1
            mini = score[i][1]


    print(cnt)