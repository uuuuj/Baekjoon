import sys

N, K = map(int, sys.stdin.readline().split())
thing = [[0, 0]]
for i in range(N):
    thing.append(list(map(int, sys.stdin.readline().split())))
dp = [[0] * (K+1) for i in range(N+1)]
#dp테이블은 w의 길이, 배낭의 허용 무게+1(0부터 탐색) 1~7 정확한 인덱스를 위해
#ex) 1kg 일때 dp[i][1] 이면 i번째 물건까지 살폈을때 허용 무게가 1인 배낭의 최대 가치
for i in range(1, N+1):
    for j in range(1, K+1):
        w = thing[i][0]
        v = thing[i][1]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])



print(dp[-1][-1])
#j - weight가 0미만이면 dp테이블에 0
#그렇지 않다면 dp[i-1][j]와 dp[i-1][j-weight] + value 값을 비교해서 더 큰 값으로 업데이트
