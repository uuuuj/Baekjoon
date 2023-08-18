import sys
from collections import deque

N = int(sys.stdin.readline())
card = deque([i for i in range(1, N+1)])

while len(card) != 1:
    card.popleft()
    move_card = card.popleft()
    card.append(move_card)
print(card[0])
