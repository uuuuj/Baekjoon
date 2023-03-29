N = int(input())
nul = N
num = 1
for i in range(N-1):
    print(' ' * (nul-1) + '*' * num)
    num += 2
    nul -= 1
nul = 0
for i in range(N):
    print(' ' * nul + '*' * num)
    num -= 2
    nul += 1