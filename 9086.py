T = int(input())
ch = []
for i in range(T):
    ch.append(input())
for _ in range(T):
    voca = ch.pop(0)
    print(voca[0]+voca[-1])


