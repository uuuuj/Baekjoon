import sys
import collections
import heapq

sys.setrecursionlimit(10**6)
#n = 노드 수, m = 간선 수
n, m = map(int, sys.stdin.readline().split())
#빈 그래프 생성
graph = collections.defaultdict(list)
#노드의 방문 정보 초기화
visited = [0] * (n+1)

#무방향 그래프 생성
#간선 정보 입력 받기
for i in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([w, u, v])
    graph[v].append([w, v, u])
#프림 알고리즘
def prim(graph, start_node):
    visited[start_node] = 1#방문 갱신
    candidate = graph[start_node] #인접 간선 추출
    heapq.heapify(candidate) #우선 순위 큐 생성
    mst = []
    total_weight = 0 #전체 가중치
    while candidate:
        w, u, v = heapq.heappop(candidate) #가중치가 가장 적은 간선 추출
        if visited[v] == 0:#방문하지 않았다면
            visited[v] = 1 #방문 갱신
            mst.append([u, v]) #mst삽입
            total_weight += w #전체 가중치 업데이트

            for edge in graph[v]: #다음 인접 간선 탐색
                if visited[edge[2]] == 0: #방문한 노드가 아니라면,(순환방지)
                    heapq.heappush(candidate, edge) #우선 순위 큐에 edge삽입
    return total_weight
print(prim(graph, 1))
