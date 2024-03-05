import sys

N, M = map(int, sys.stdin.readline().split())
A = []
for i in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
M, K = map(int, sys.stdin.readline().split())
B = []
for i in range(M):
    B.append(list(map(int, sys.stdin.readline().split())))

C = [[0] * K for i in range(N)]
for row in range(N):
    for col in range(K):
        e = 0
        for i in range(M):
            e += A[row][i] * B[i][col]
        C[row][col] = e


for j in C:
    print(*j)

