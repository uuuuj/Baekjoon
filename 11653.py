N = int(input())

if N % 2 == 0:
    mok = N // 2
    if mok % 2 == 0:
        mok = mok // 2
elif N % 3 == 0:
    num = N / 3
