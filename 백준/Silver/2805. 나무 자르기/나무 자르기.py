import sys

N, M = map(int, sys.stdin.readline().split())
arr= list(map(int, sys.stdin.readline().split()))
#가장 짧은 길이 1을 st로 가장 긴 길이를 end로


st = 1
en = max(arr)

#이분 탐색이 끝날때까지 while문을 돌린다
while st <= en:
    hap = 0
    mid = (st+en)//2
    for i in arr:
        if i >= mid:
            hap += i - mid
    if hap >= M:
        st = mid + 1
    else:
        en = mid - 1

print(en)
#mid를 st와 en의 중간으로 두고, 모든 값에서 mid를 빼 총 어느정도 길이의 벌목된 나무가 나오나 살펴본다
#벌목나무가 목표치 이상이면 md+1을 st로 두고 다시 while문 반복
#벌목나무가 목표치 이하면 mid-1을 en으로 두고 다시 while문 반복
#st와 en이 같아지면 조건을 만족하는 최대의 나무 절단 높이를 찾으면 탈출한다
#결과 값인 en출력

