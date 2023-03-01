T = int(input())

for i in range(T):
    R, S = input().split()
    New = ''
    for j in range(0, len(S)):
        New = New + S[j]*int(R)
        if j == len(S)-1:
            print(New)
