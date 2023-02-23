N, M = map(int, input().split())
i = [0 for num in range(M)]
j = [0 for num in range(M)]
k = [0 for num in range(M)]
for num in range(M):
    i[num], j[num], k[num] = map(int, input().split())
print(i)
print(j)
print(k)
breakpoint()
i, j, k = map(int, input().split())
basket = [0 for num in range(N)]

for i in range(j):
    basket[i] = k

