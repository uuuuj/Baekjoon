import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in num:
    error = 0
    if i > 1:

        for j in range(2, i):
            if i % j == 0:
                error += 1
        if error == 0:
            cnt += 1

print(cnt)