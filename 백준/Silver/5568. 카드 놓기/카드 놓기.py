import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
card = []
for i in range(N):
    card.append(sys.stdin.readline().strip())


new_card = []

def pick_card(result, n, picked):
    if n == K:
        if result not in new_card:
            new_card.append(result)
        return
    for i in range(N):
        if i not in picked:
            picked.append(i)
            new_result = result + card[i]
            pick_card(new_result, n+1, picked)
            picked.pop()

pick_card('', 0,[])
print(len(new_card))