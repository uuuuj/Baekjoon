import sys

n = int(sys.stdin.readline())

location = [0] + list(map(int, sys.stdin.readline().strip()))
ans = 0
graph = [[]for i in range(n+1)]
visited = [False] * (n+1)
for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    #둘다 실내인 경우
    if location[a] == 1 and location[b] == 1:
        ans += 2
#v:정점 번호 cnt : 실외와 연결된 실내개수 카운트
def dfs(v, cnt):
    visited[v] = True
    for i in graph[v]:
        if location[i] == 1: #해당 노드의 위치가 실내이면
            cnt += 1
        elif not visited[i] and location[i] == 0: #방문하지 않았고, 해당 지점의 위치가 실외라면
            cnt = dfs(i, cnt)
    return cnt

sum = 0

for i in range(1, n+1):
    if not visited[i] and location[i] == 0: #실외를 기준으로
        x = dfs(i, 0) #현재 cnt는 0
        sum += x*(x-1) #실외인 노드를 기준으로 인접 노드 개수 세기
print(sum+ans)
