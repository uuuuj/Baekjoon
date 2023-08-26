import sys
#T : 테스트 케이스 개수
T = int(sys.stdin.readline())
for i in range(T):
    #동전 가지 수
    N = int(sys.stdin.readline())
    #동전 종류
    coins = list(map(int, sys.stdin.readline().split()))
    #만들어야하는 금액
    M = int(sys.stdin.readline())
    dp = [0] * (M+1)
    dp[0] = 1
    for coin in coins:
        for i in range(1, M+1):
            if i - coin >= 0:
                dp[i] = dp[i] + dp[i-coin]
    print(dp[M])

