#방문하지 않았을 경우 방문처리하고 그 위치까지의 거리를 +1해준다.
# 그 뒤 +1해준 거리가 목표 거리 K와 같아질 경우 answer라는 리스트에 넣은 뒤
# 오름차순으로 정렬하고 while 문 밖 if문에서 프린트해주도록했다.
import sys
from collections import deque
def bfs(start):
    ans = []
    q = deque([start])
    visited[start] = True
    dist_list[start] = 0
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                dist_list[i] = dist_list[node] + 1
                if dist_list[i] == K:
                    ans.append(i)
    if len(ans) == 0:
        print(-1)
    else:
        ans.sort()
        for i in ans:
            print(i, end = " ")


N, M, K, X = map(int, sys.stdin.readline().split())
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
dist_list = [0] * (N+1)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

bfs(X)