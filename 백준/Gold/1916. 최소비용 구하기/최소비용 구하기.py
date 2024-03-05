import heapq, sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for i in range(N+1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    #a:출발 노드, b: 도착노드, c:비용
    graph[a].append([b, c])
#시작, 출발
st, en = map(int, sys.stdin.readline().split())
#거리를 최대값으로 설정
dist = [1e9] * (N+1)

def dijkstra(start):
    #시작 지점의 비용은 0으로 설정
    dist[start] = 0
    #시작 지점 비용, 시작 지점 번호
    q = [(0, st)]
    while q:
        #w:현재 지점의 코스트, cur:현재 지점의 번호
        w, cur = heapq.heappop(q)
        if dist[cur] < w:
            continue
        for dest, wei in graph[cur]:
            #현재 지점의 코스트와 다음 지점의 코스트의 합
            cost = dist[cur] + wei
            #만약 다음 지점의 코스트가 현재 지점 -> 다음 지점의 코스트보다 크면 더 작은 값으로 업데이트
            if dist[dest] > cost:
                dist[dest] = cost
                #더 작은 값으로 업데이트했기 때문에 dest도 그 다음 지점으로 갈 수 있음.
                heapq.heappush(q, (cost, dest))

dijkstra(st)
print(dist[en])

