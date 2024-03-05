#노드 정보들을 받고
import sys
sys.setrecursionlimit(10**6)
K = int(sys.stdin.readline())

def DFS(graph, v, visited, group):
    visited[v] = group
    for i in graph[v]:
        #방문 안한 상태라면
        if visited[i] == 0:
            #현재 노드의 그룹과 다른 값 전달
            result = DFS(graph, i, visited, -group)
            if not result:#result가 False라면 즉 이분 그래프가 아니라면
                return False
        else:#연결된 노드와 그룹이 같다면
            if visited[i] == group:
                return False
    return True


for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V+1):
        if visited[i] == 0:
            result = (DFS(graph, i, visited, 1))
            if not result:
                break
    print('YES') if result else print('NO')


