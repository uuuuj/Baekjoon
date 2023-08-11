import sys

T = int(sys.stdin.readline())

for i in range(T):
    score = 0
    plus = []
    data = list(input())
    for j in data:
        if j == 'O':
            score += 1
            plus.append(score)
        else:
            score = 0

    for k in plus:
        score = sum(plus)

    print(score)

