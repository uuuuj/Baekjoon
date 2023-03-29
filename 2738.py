N, M = map(int, input().split())
A = []
B = []
hap = []
zero = [0 for i in range(M)]
for i in range(N):
    hap.append(list(map(int, zero)))

for i in range(N):
    A.append(list(map(int, input().split())))

for i in range(N):
    B.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        hap[i][j] = A[i][j] + B[i][j]

for i in range(N):
    print(*hap[i])
