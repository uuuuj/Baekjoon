import sys

W, H = map(int, sys.stdin.readline().split())

T = int(sys.stdin.readline())

x = [0, W]
y = [0, H]

for i in range(T):
    direction, coord = map(int, sys.stdin.readline().split())
    if direction == 0:
        y.append(coord)

    else:
        x.append(coord)

x.sort(reverse=True)
y.sort(reverse=True)

max_x = 0
max_y = 0
for i in range(len(x)-1):
    if max_x < x[i] - x[i+1]:
        max_x = x[i] - x[i+1]

for i in range(len(y)-1):
    if y[i] == y[-1]:
        break
    if max_y < y[i] - y[i+1]:
        max_y = y[i] - y[i+1]

print(max_x * max_y)
