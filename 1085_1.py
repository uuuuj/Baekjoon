import sys

x, y, w, h = map(int, sys.stdin.readline().split())

A = h - y
B = w - x
C = y - 0
D = x - 0

print(min(A, B, C, D))

