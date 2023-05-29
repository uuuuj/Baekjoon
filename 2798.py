import sys
import time
start = time.time()

N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if card[i] + card[j] + card[k] > M:
                continue
            else:
                result = max(result, card[i] + card[j] + card[k])

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
print(result)