import sys
from collections import deque

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        node = q.popleft()
        #노드와 연결된 노드들 확인
        for i in graph[node]:
            #방문안했다면
            if not visited[i]:
                visited[i] = True
                #검사해야하는 컴퓨터(노드)를 append
                q.append(i)

#컴퓨터의 수
N = int(sys.stdin.readline())
#컴퓨터 쌍의 수 = 간선의 갯수
M = int(sys.stdin.readline())

graph = [[] for i in range(N+1)]
count = 0
visited = [False] * (N+1)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


bfs(1)
count = visited.count(True) - 1


print(count)