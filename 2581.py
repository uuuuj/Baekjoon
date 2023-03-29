M = int(input())
N = int(input())

lst = []
for i in range(N-M+1):
    lst.append([])

k = 0
for i in range(M, N+1):
    for j in range(1, i+1):
        if i % j == 0:
            lst[k].append(j)
    k += 1
hap = 0
sosu = []
for i in range(len(lst)):
    if len(lst[i]) == 2:
       hap += lst[i][1]
       sosu.append(lst[i][1])
    else:
        pass
if hap == 0:
    print(-1)
else:
    print(hap)
    print(min(sosu))