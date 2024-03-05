import sys

N, K = map(int, sys.stdin.readline().split())
num = list(sys.stdin.readline().strip())
stack = []

for i in num:
    while stack and K > 0 and stack[-1] < i:
        stack.pop()
        K -= 1
    stack.append(i)

print(''.join(stack[:len(stack)-K]))
