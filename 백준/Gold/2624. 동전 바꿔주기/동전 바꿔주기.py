import sys

T = int(sys.stdin.readline())
k = int(sys.stdin.readline())
coins = []
for i in range(k):
    a, b = map(int, sys.stdin.readline().split())
    coins.append([a, b])
dp = [0] * (T+1)
dp[0] = 1
for coin, cnt in coins:
    for money in range(T, 0, -1):
        for i in range(1, cnt+1):
            if money - coin * i >= 0:
                dp[money] += dp[money-coin*i]
print(dp[T])