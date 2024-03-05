import sys

n = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
arr = []
visited = [False] * n

max_ans = float('-inf')


def dfs(depth):
    global max_ans
    if depth == n:
        ans = 0
        for i in range(n - 1):
            ans += abs(graph[arr[i]] - graph[arr[i + 1]])
        max_ans = max(max_ans, ans)
        return
    for i in range(n):
        #visited[i] 가 False라면
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            dfs(depth + 1)
            visited[i] = False
            arr.pop()


dfs(0)
print(max_ans)