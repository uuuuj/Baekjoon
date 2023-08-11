import sys

N = int(sys.stdin.readline())
cnt = 99
if N < 100:
    print(N)
elif N == 100:
    print(99)
else:
    for i in range(101, N+1):
        A = (i // 100) - (i%100)//10
        B = ((i%100)//10) - ((i%100)%10)
        if A == B:
            cnt += 1
        else:
            cnt += 0
    print(cnt)
