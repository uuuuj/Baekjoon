S = input()
cnt = S.count(' ') + 1
if S[0] == ' ':
    cnt = cnt - 1
if S[-1] == ' ':
    cnt = cnt - 1
print(cnt)