import sys
from typing import MutableSequence
def bubble_sort(n: MutableSequence) -> None:
    for i in range(len(n)):
        for j in range(len(n)-1, i, -1):
            if n[j-1] > n[j]:
                n[j-1], n[j] = n[j], n[j-1]
num = []
N = int(sys.stdin.readline())
for i in range(N):
    num.append(int(sys.stdin.readline()))

bubble_sort(num)

for i in num:
    print(i)