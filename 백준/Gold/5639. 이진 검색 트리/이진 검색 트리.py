import sys
sys.setrecursionlimit(10 ** 9)

pre = []
while True:
    try:
        pre.append(int(sys.stdin.readline()))
    except:
        break

def post(st, en):
    if st > en:
        return
    mid = en + 1
    for i in range(st + 1, en + 1):
        if pre[i] > pre[st]:
            mid = i
            break
    post(st + 1, mid - 1)#왼쪽 트리
    post(mid, en)#오른쪽 트리
    print(pre[st])#루트 노드

post(0, len(pre)-1)


