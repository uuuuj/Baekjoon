import sys
from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft() #가장 작은 원소 제거
        print(v, end=" ")
        for i in range(1, n + 1):
            if visited[i] == 0 and graph[v][i] == 1: #방문한 적이 없고,
                q.append(i)
                visited[i] = 1
def dfs(v):
    visited2[v] = 1
    print(v, end=" ")
    for i in range(1, n+1):
        if visited2[i] == 0 and graph[v][i] == 1:
            dfs(i)

n, m, v = map(int, sys.stdin.readline().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
visited2 = [0] * (n + 1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1
    

dfs(v)
print()
bfs(v)



