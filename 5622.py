S = list(input())
cnt = 0
S_ascii = 0
for i in range(len(S)):
    S_ascii = ord(S[i])
    if 65 <= S_ascii <= 67:
        cnt += 3
    elif 68 <= S_ascii <= 70:
        cnt += 4
    elif 71 <= S_ascii <= 73:
        cnt += 5
    elif 74 <= S_ascii <= 76:
        cnt += 6
    elif 77 <= S_ascii <= 79:
        cnt += 7
    elif 80 <= S_ascii <= 83:
        cnt += 8
    elif 84 <= S_ascii <= 86:
        cnt += 9
    elif 87 <= S_ascii <= 90:
        cnt += 10

print(cnt)