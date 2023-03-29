S = input()
S_rev = S
S_rev2 = list(S_rev)
S_rev2.reverse()
S_rev3 = ''.join(S_rev2)

if S == S_rev3:
    print(1)
else:
    print(0)
