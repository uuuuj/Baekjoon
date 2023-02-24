N, M = map(int, input().split())
basket = [0] * (N+1)
for n in range(1, N+1):
    basket[n] = n
for _ in range(M):
    i, j = map(int, input().split())
    basket[i], basket[j] = basket[j], basket[i]

for n in range(1, N+1):
    print(basket[n], end=" ")