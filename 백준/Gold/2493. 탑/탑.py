import sys

N = int(sys.stdin.readline())

tower = list(map(int, sys.stdin.readline().split()))
result = []
stack = []
ans = []

for i in range(N):
    while stack:
        #stack의 [-1][1]은 스택의 가장 위에 올라와있는 탑의 높이. 즉 가장 최신에 업데이트된 탑의 정보
        #현재 stack에 있는 탑이 tower보다 큰 경우는 수신이 가능한 상황
        if stack[-1][1] > tower[i]: #수신 가능 상황
            ans.append(stack[-1][0] + 1) #탑의 인덱스에 +1을 해주면 탑의 번호가 됨. 그걸 ans에 append
            break
        else:
            stack.pop()#수신 불가능한 상황 ->
    if not stack: #스택이 비면 레이저를 수신할 탑이 없다
        ans.append(0)
    stack.append([i, tower[i]]) #인덱스, 값
print(" ".join(map(str, ans)))
