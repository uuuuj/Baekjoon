import sys
import heapq
n = int(sys.stdin.readline())
cupnoodle = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    cupnoodle.append([a, b])
cupnoodle.sort(key=lambda x:(x[0]))
q = []

for i in range(n):
    heapq.heappush(q, cupnoodle[i][1])
    if cupnoodle[i][0] < len(q):
        heapq.heappop(q)

print(sum(q))