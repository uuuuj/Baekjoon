N, K = map(int, input().split())
yak = []
for i in range(1, N+1):
    if N % i == 0:
        yak.append(N // i)
    else:
        pass

yak.sort()

if len(yak) < K:
    print(0)
else:
    print(yak[K-1])

