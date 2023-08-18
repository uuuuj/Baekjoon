import sys

from collections import deque

N, K = map(int, sys.stdin.readline().split())
Josephus = []
dq = deque([i for i in range(1, N+1)])
while len(dq) > 1:
    dq.rotate(-(K-1))
    Josephus.append(dq[0])
    dq.popleft()

Josephus.append(dq[0])
print('<', end="")
for i in range(N):
    if i == N-1:
        print(f'{Josephus[i]}>')
    else:
        print(f'{Josephus[i]}, ', end="")


