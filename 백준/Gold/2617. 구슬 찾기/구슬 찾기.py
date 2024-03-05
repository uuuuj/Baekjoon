import sys

n, m = map(int, sys.stdin.readline().split())
heavy = [[]for i in range(n+1)]
light = [[]for i in range(n+1)]
for i in range(m):
    h, l = map(int, sys.stdin.readline().split())
    heavy[l].append(h)
    light[h].append(l)

def dfs(node, list):
    global check, visited
    visited[node] = 1
    for j in list[node]:
        if visited[j] == 0:
            check += 1
            dfs(j, list)
mid = (n+1)/2
count = 0
for i in range(1, n+1):
    visited = [0] * (n + 1)
    check = 0
    dfs(i, heavy)
    if check >= mid:
        count += 1
    check = 0
    dfs(i, light)
    if check >= mid:
        count += 1
print(count)