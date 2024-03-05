import sys
from functools import cache

S = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())
A = []
for i in range(n):
    A.append(list(sys.stdin.readline().strip()))
dp = [0] * 101
@cache
def rec(cur):
    global S
    for a in A:
        length = len(a)
        if S[cur:cur+length] == a:
            for k in range(cur, cur+length):
                dp[k] = 1
            rec(cur+length)
    return
rec(0)
print(dp[len(S)-1])
