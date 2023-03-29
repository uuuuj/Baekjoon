C = int(input())
N = []
for i in range(C):
    N.append(list(map(int, input().split())))
print(N)
j = 0
for j in range(C):
    cnt = 0
    hap = 0
    k = 1
    for x in range(1, N[j][0]+1):
        hap += N[j][x]
    avg = hap / N[j][0]
    for k in range(1, len(N[j])):
        if N[j][k] > avg:
            cnt += 1

    per = round((cnt / N[j][0]) * 100, 3)
    print(f'{per:.3f}' + '%')


