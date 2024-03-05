import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

A.sort()

M = int(sys.stdin.readline())
A_2 = list(map(int, sys.stdin.readline().split()))


def search(target):
    st = 0
    en = N - 1
    mid = int((st + en) // 2)
    while st <= en:
        if A[st] == target or A[en] == target or A[mid] == target or A[st] == A[en] == A[mid] == target:
            return 1
        else:
            mid = int((st + en) // 2)
            if target > A[mid]:
                st = mid+1
            else:
                en = mid - 1
    return 0

for i in A_2:
    print(search(i))



