import sys

hund_height = []
hegiht = [int(sys.stdin.readline()) for i in range(9)]
k = 7
#hap : 키의 총합
#n :뽑은 난쟁이 수
#picked: 이미 뽑은 난쟁이들의 idx배열
def search(hap, n, picked):
    #n이 k가 되면 카드를 모두 뽑은 것
    if n == k:
        if hap == 100:
            for idx in picked:
                hund_height.append(hegiht[idx])
            hund_height.sort()
            for idx in hund_height:
                print(idx)
            sys.exit()
        else:
            return
    for list_idx in range(9):
        if list_idx not in picked:
            picked.append(list_idx)
            new_hap = hap + hegiht[list_idx]
            search(new_hap, n+1, picked)
            picked.pop()

search(0, 0, [])



