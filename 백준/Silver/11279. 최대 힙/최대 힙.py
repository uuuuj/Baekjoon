import sys

import heapq

N = int(sys.stdin.readline())
dq = []

for i in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(dq) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(dq))


    else:
        heapq.heappush(dq, -x)
