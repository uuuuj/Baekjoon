import sys

N = int(sys.stdin.readline())
gop = [i for i in range(1, N+1)]
ans = 1
for i in gop:
    ans *= i

print(ans)
