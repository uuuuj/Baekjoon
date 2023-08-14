import sys

N, M = map(int, sys.stdin.readline().split())


num = [i for i in range(1, N + 1)]

def back_tracking(n, picked):
    if n == M:
        for idx in picked:
            print(num[idx], end=" ")
        print(sep='\n')
        return
    for num_idx in range(len(num)):
        if num_idx not in picked:
            picked.append(num_idx)
            back_tracking(n+1, picked)
            picked.pop()

back_tracking(0, [])