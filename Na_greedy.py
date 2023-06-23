N, M, K = map(int, input().split())
N_array = list(map(int, input().split()))

N_array.sort()
hap = 0

First = N_array[-1]
Second = N_array[-2]

while True:
    for i in range(K):
        if M == 0:
            break
        hap += First
        M -= 1
    if M == 0:
        break
    hap += Second
    M -= 1

print(hap)
