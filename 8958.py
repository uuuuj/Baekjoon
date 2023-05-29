N = int(input())

for i in range(N):
    score = 0
    hap = 0
    M = input()
    for j in range(len(M)):
        if M[j] == 'O':
            score += 1
        else:
            score = 0
        hap = hap + score
    print(hap)

