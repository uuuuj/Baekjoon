import sys

N = int(sys.stdin.readline())

cost_array = []

for i in range(N):
    array = list(map(int, sys.stdin.readline().split()))
    cost_array.append(array)

visited = [False] * N
#초기값 업데이트를 저장하는 전역변수
min_cost = 1e9
def dfs(depth, start, cost):
    #전역변수를 업데이트할때
    global min_cost
    if depth == N-1 and cost_array[start][0] != 0:
        min_cost = min(min_cost, cost + cost_array[start][0])
        return
    for i in range(N):
        if not visited[i] and cost_array[start][i] != 0:
            visited[i] = True
            dfs(depth+1, i, cost + cost_array[start][i])
            visited[i] = False

visited[0] = True

dfs(0,0,0)
print(min_cost)