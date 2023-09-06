import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

cards = []

for i in range(n):
    cards.append(sys.stdin.readline().strip())

new_card = []
#함수 선언
def picked_card(result, picked, m):
    if m == k:
        if result not in new_card:
            new_card.append(result)
        return
    for i in range(n):
        if i not in picked:
            picked.append(i)
            new_result = result + cards[i]
            picked_card(new_result, picked, m+1)
            picked.pop()


picked_card('', [], 0)
print(len(new_card))

#picked안에 i가 없다면

#뽑은 카드 리스트에 해당 카드 번호를 append
#새로 만든 숫자
#재귀함수 호출
#종료조건 n==k가 되면
