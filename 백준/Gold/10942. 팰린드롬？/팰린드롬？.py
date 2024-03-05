import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
st_en = []


dp = [[0] * n for i in range(n)]

for Len in range(n):
    for st in range(n-Len):
        end = st + Len
        #하나일 경우
        if end == st:
            dp[st][end] = 1
        elif numbers[st] == numbers[end]:
            if st+1 == end:
                dp[st][end] = 1
            elif dp[st+1][end-1] == 1:
                dp[st][end] = 1

for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s-1][e-1])