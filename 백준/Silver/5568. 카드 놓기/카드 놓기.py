import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

#주어지는 카드
card = []
#새로 생성한 수
new_card = []

for i in range(n):
    card.append(sys.stdin.readline().strip())

#result: 카드를 합쳐 만든 문자
#n: 뽑은 카드 수
#picked: 이미 뽑은 카드의 idx 배열
def make_number(result, n, picked):
    #n이 k가 되면 카드를 모두 뽑은 것
    if n == k:
        #이미 뽑은 카드와 겹치는 지 확인하고,
        if result not in new_card:
            #겹치지 않으면 카드 배열에 추가
            new_card.append(result)
            # print(new_card)
        return
    for card_idx in range(len(card)):
        #picked에 card_idx가 있으면 이미 뽑은 카드니까 제외
        if card_idx not in picked:
            #지금 뽑은 카드의 idx를 뽑은 카드의 idx 배열에 추가
            picked.append(card_idx)

            #지금 뽑은 카드의 값을 기존에 뽑은 값들 뒤에 더해서 새 변수에 할당
            new_result = result + card[card_idx]
            # print(new_result)
            #지금 완성된 카드값, 뽑은 카드 수, 사용한 카드의 idx들
            make_number(new_result, n+1, picked)
            #다음 반복에서는 다른 카드를 뽑을거니까 지금 뽑은 카드의 idx를 제거
            picked.pop()


make_number("", 0, [])
print(len(new_card))
