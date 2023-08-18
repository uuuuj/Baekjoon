import sys
from collections import deque

N = int(sys.stdin.readline())
Q = deque([])
for i in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push':
        Q.append(command[1])
    if command[0] == 'front':
        if not Q:
            print(-1)
        else:
            print(Q[0])
    if command[0] == 'back':
        if not Q:
            print(-1)
        else:
            print(Q[-1])
    if command[0] == 'pop':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[0])
            del Q[0]
    if command[0] == 'size':
        print(len(Q))
    if command[0] == 'empty':
        if len(Q) == 0:
            print(1)
        else:
            print(0)
