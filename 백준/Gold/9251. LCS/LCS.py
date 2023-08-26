import sys

X = list(sys.stdin.readline().strip())
Y = list(sys.stdin.readline().strip())
max_len = max(len(X), len(Y))

dp = [[0] * (len(X)+1) for i in range(len(Y)+1)]

for i in range(1, len(Y)+1):
    for j in range(1, len(X)+1):
        if Y[i-1] == X[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])
