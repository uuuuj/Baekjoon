import sys
coord_x = []
coord_y = []
n = int(input())

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    coord_x.append(x)
    coord_y.append(y)

if n == 1:
    print(0)
else:
    x_ans = max(coord_x) - min(coord_x)
    y_ans = max(coord_y) - min(coord_y)
    print(x_ans * y_ans)