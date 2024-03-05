import sys

A, B = map(int, sys.stdin.readline().split())

N = int(sys.stdin.readline())
width = [0, A]
height = [0, B]
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if x == 0:
        height.append(y)
    else:
        width.append(y)

width.sort(reverse=True)
height.sort(reverse=True)
max_w = 0
max_h = 0
for i in range(len(width)-1):
    if max_w < width[i] - width[i+1]:
        max_w = width[i] - width[i+1]
    else:
        continue

for i in range(len(height)-1):
    if max_h < height[i] - height[i+1]:
        max_h = height[i] - height[i+1]
    else:
        continue

print(max_h * max_w)
