import sys

N = int(sys.stdin.readline())
stick = []
cnt = 1
for i in range(N):
    stick.append(int(sys.stdin.readline()))
right = stick[-1]
for i in reversed(range(N)):
    if stick[i] > right:
        cnt += 1
        right = stick[i]

print(cnt)