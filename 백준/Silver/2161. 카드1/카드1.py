import sys
from collections import deque
N = int(sys.stdin.readline())
cards = [i for i in range(1, N+1)]
q = deque()
for i in range(1, N+1):
    q.append(i)
while q:
    # Print and remove the top card
    print(q.popleft(), end=" ")

    # If there are no cards left, break out
    if not q:
        break

    # Move the top card to the bottom
    q.rotate(-1)





