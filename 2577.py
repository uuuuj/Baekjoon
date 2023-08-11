import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
gop = A*B*C
result = list(map(int, str(gop)))



for j in range(0, 10):
    cnt = 0
    for i in result:
        if i == j:
            cnt += 1
    print(cnt)

