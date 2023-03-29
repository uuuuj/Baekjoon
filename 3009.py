import sys
coord = []
coord_x = []
coord_y = []
ans = []
for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    coord_x.append(x)
    coord_y.append(y)

for i in range(len(coord_x)):
    cnt = coord_x.count(coord_x[i])
    if cnt == 1:
        ans.append(coord_x[i])
        break

cnt = 0

for i in range(len(coord_y)):
    cnt = coord_y.count(coord_y[i])
    if cnt == 1:
        ans.append(coord_y[i])
        break

print(*ans)