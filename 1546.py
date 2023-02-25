N = int(input())
score = (input().split())

for i in range(N):
    score[i] = int(score[i])

max_sub = max(score)
hap = 0
for i in range(N):
    score[i] = ((score[i])/max_sub)*100
    hap = hap + score[i]
print(hap/N)