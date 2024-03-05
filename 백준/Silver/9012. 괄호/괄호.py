#문자열을 검색해서 여는 괄호이면 스택에 넣고, 닫는 괄호이면 스택을 pop()한다.
#이때, pop()할 원소가 없다면 열지도 않은 괄호를 닫은 것이기에 boolean 값을 False로 초기화 하고, 반복문을 탈출한다.
#모든 검사가 끝났을때 스택에 원소가 남아있으면 여는 괄호가 모두 닫히지 않은 것이기에 False로 초기화한다.
#스택에 원소가 없고isVPS가 True이면 'YES'를 그렇지 않으면 'NO'를 출력한다.
import sys

N = int(sys.stdin.readline())

for i in range(N):
    stack = []
    VPS_list = input()
    isVPS = True
    for j in VPS_list:
        if j == '(':
            stack.append(j)
        else:
            if not stack:
                isVPS = False
                break
            else:
                stack.pop()
    if not stack and isVPS:
        print('YES')
    elif stack or not isVPS:
        print('NO')
