N, M = map(int, input().split())
i = [0 for num in range(M)]
j = [0 for num in range(M)]
k = [0 for num in range(M)]
for num in range(M):
    i[num], j[num], k[num] = map(int, input().split())
for num in range(M):
    i[num] = i[num]-1
    #j[num] = j[num] - 1
basket = [0 for num in range(N)]
n = 0
print("i = ", i)
print("j = ", j)
print("k = ", k)
#크게 반복 네번하고
def save():

for num in range(M):
    print(basket)
    while n == j[n]:
        basket[n] = k[n]
    n = n + 1
print("last ", basket)

