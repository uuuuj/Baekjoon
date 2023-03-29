num = int(input())
coord = []
i = 0
for j in range(0, 100):
    lst = []
    for i in range(0, 100):
        lst.append(0)
    coord.append(lst)

for i in range(0, num):
    x, y = map(int, input().split())
    coord[x][y] = 1
    for j in range(0, 10):
        coord[x+j][y] = 1
        for k in range(0, 10):
            coord[x+j][y+k] = 1
hap = 0
for j in range(0, 100):
    hap += coord[j].count(1)
print(hap)