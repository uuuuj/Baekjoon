import sys

N, C = map(int, sys.stdin.readline().split())

arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

def search(arr, st, en):
    while st <= en:
        mid = (st+en) // 2
        current = arr[0]
        count = 1

        for i in range(1, len(arr)):
            if arr[i] >= current + mid:
                count += 1
                #공유기 설치 완료
                current = arr[i]
        #공유기 개수가 설치해야하는 개수보다 많을때 -> 즉 간격이 좁다는 것. 간격을 늘릴 수 있다는 것.
        if count >= C:
            global ans
            st = mid + 1
            ans = mid
        else:
            en = mid - 1

st = 1
en = arr[-1] - arr[0]
ans = 0

search(arr, st, en)
print(ans)