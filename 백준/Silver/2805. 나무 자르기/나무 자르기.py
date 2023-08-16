import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
#가장 짧은 길이 1을 st로 가장 긴 길이를 end로


st = 1
en = max(arr)


while st <= en:
    hap = 0
    mid = (st + en) // 2
    for i in arr:
        if i >= mid:
            hap += i - mid
    if hap >= M:
        st = mid + 1
    else:
        en = mid - 1

print(en)
