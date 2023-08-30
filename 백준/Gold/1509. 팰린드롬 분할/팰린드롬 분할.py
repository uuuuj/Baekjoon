import sys
#rstrip을 붙이려고!
input = lambda: sys.stdin.readline().rstrip()
t = input()     # 문자열 리스트
n = len(t)      # 문자열 길이
dp = [2500 for _ in range(n+1)]
dp[-1] = 0
is_p = [[0 for j in range(n)] for i in range(n)]  # 팰린드롬?
# 한자릿수 팰린드롬
for i in range(n):
    is_p[i][i] = 1
# 두자릿수 팰린드롬
for i in range(n-1):
    # 같은 숫자면 팰린드롬
    if t[i] == t[i+1]:
        is_p[i][i+1] = 1
# 길이 3~n 짜리 팰린드롬
for l in range(3, n+1):
    for start in range(n-l+1):
        end = start+l-1
        # 처음과 끝 숫자가 같고, 그 사이가 팰린드롬이면
        if t[start] == t[end] and is_p[start+1][end-1]:
            is_p[start][end] = 1
for end in range(n):
    for start in range(end+1):  # start부터 end까지
        if is_p[start][end]:    # 팰린드롬이면
            # 이 부분 이해 X
            dp[end] = min(dp[end], dp[start-1]+1)   # 분할 갯수 최소값
        else:
            dp[end] = min(dp[end], dp[end-1]+1)
print(dp[n-1])