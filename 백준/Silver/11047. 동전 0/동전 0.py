import sys

n, k = map(int, sys.stdin.readline().split())
A = []

for i in range(n):
    a = int(sys.stdin.readline())
    A.append(a)
ans = 0
# 가장 큰 동전부터 시작해서 몫을 카운트해주고 나머지 동전을 내림차순으로 반복한다
for i in reversed(A):
    if k == 0:
        break
    ans += k // i
    k = k % i
print(ans)
