import sys

#행렬 크기 입력
n, m = map(int,sys.stdin.readline().split())
#DP 테이블
dp = [[0] * m for i in range(n)]
#DP 테이블에 각 행 추가
for i in range(n):
    dp[i] = list(map(int, sys.stdin.readline().split()))

for j in range(1, m):
    dp[0][j] += dp[0][j-1]

#DP 테이블의 나머지 행 업데이트

#두가지 임시 배열 생성. 같은 배열 두개 만들어서 각각 비교
for i in range(1, n):
    # 왼쪽에서 오른쪽으로 가는 경우
    LR = dp[i][:]
    #오른쪽에서 왼쪽으로 가는 경우
    RL = dp[i][:]
    #왼쪽에서 오른쪽으로 가는 경우 업데이트
    for j in range(m):
        #첫번째 열일 경우, 위에서 오는 경우밖에 없으므로
        if j == 0:
            LR[j] += dp[i-1][j]
        #나머지 열에 대해 위에서 내려오는 경우와 왼쪽에서 오는 경우를 비교
        else:
            LR[j] += max(dp[i-1][j], LR[j-1])
        #오른쪽에서 왼쪽으로 가는 경우 업데이트
    for j in range(m-1, -1, -1):
        #마지막 열일 경우, 위에서 오는 경우 밖에 없으므로
        if j == (m-1):
            RL[j] += dp[i-1][j]
        #나머지 열에 대해, 위에서 내려오는 경우와 오른쪽에서 오는 경우를 비교
        else:
            RL[j] += max(dp[i-1][j], RL[j+1])
    #두가지 임시 배열을 비교해, 각 좌표값들을 최대 값으로 업데이트
    for j in range(m):
        dp[i][j] = max(LR[j], RL[j])
print(dp[n-1][m-1])