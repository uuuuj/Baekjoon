import sys
#줄의 개수 N
N = int(sys.stdin.readline())
#N개의 수로 이루어진 수열
A = list(map(int, sys.stdin.readline().split()))
#N-1개의 수로 이루어진 연산자의 갯수. 차례대로 +, -, x, %
num_op = list(map(int, sys.stdin.readline().split()))

max_result = -1e9
min_result = 1e9

def dfs(depth, total, plus, minus, multi, divide):
    global max_result, min_result
    if depth == N:
        max_result = max(total, max_result)
        min_result = min(total, min_result)
        return
    #인자가 0이 아닌 경우에만 실행된다.
    if plus:
        dfs(depth + 1, total + A[depth], plus -1, minus, multi, divide)
    if minus:
        dfs(depth + 1, total - A[depth], plus, minus - 1, multi, divide)
    if multi:
        dfs(depth+1, total * A[depth], plus, minus, multi - 1, divide)
    if divide:
        dfs(depth+1, int(total / A[depth]), plus, minus, multi, divide -1)

dfs(1, A[0], num_op[0], num_op[1], num_op[2], num_op[3])

print(max_result)
print(min_result)