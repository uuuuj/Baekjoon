import sys

n, k = map(int, sys.stdin.readline().split())

elec = list(map(int, sys.stdin.readline().split()))
cnt = 0
multitab = []
swap = 0
result = 0
num = 0
max_l = 0
for i in elec:
    if i in multitab:
        pass
    elif len(multitab) < n:
        multitab.append(i)
    elif len(multitab) == n:
        #멀티탭에 꽂힌 전자제품 리스트 확인
        for m in multitab:
            #만약 해당 제품이 elec[자기자신+1:끝] 안에 없다면, swap해도 되기 때문에 swap변수에 저장
            if m not in elec[num:]:
                swap = m
                break
            elif elec[num:].index(m) > max_l:
                max_l = elec[num:].index(m)
                swap = m
                # 그리고 swap에 저장했던 멀티탭의 인덱스에 현재 꽂아야하는 제품 넣기
        multitab[multitab.index(swap)] = i
        swap = 0
        max_l = 0
        result += 1

    num += 1
print(result)