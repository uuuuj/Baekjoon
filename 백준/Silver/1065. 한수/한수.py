import sys

N = int(sys.stdin.readline())
cnt = 99
if N < 100:
    cnt = N
    print(cnt)
elif 100 == N:
    print(99)
else:
    for i in range(101, N+1):
        if (i // 100) - (i % 100) // 10 == ( (i % 100) // 10 ) - ((i % 100) % 10):
            cnt += 1
        else:
            cnt += 0
    print(cnt)