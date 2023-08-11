N = int(input())
lst = []
num = list(map(int, input().split()))
for i in range(N):
    lst.append([])
for i in range(0, N):
    for j in range(1, num[i]+1):
        if num[i] % j == 0:
            lst[i].append(j)
cnt = 0
for i in range(N):
    if len(lst[i]) == 2:
        cnt += 1
    else:
        pass
print(cnt)