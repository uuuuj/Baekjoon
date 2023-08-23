import sys
from collections import deque
input = sys.stdin.readline
n = int(input())  # 보드의 크기 N x N
k = int(input())  # 사과의 개수
apple = []  # 사과 위치가 저장된 리스트
for _ in range(k):
    a, b = map(int, input().split())
    apple.append((a-1, b-1))
l = int(input())  # 방향 변환 횟수
turninfo = {}  # 방향 변환 정보
for _ in range(l):
    a, b = input().split()
    turninfo[int(a)] = b
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
body = [[0]*n for _ in range(n)]  # 뱀의 몸이 존재하는 위치를 나타내기 위한 리스트
t = 0  # 게임 진행 시간
d = 0  # 처음은 오른쪽으로 이동
def turn(t):
    global d
    if turninfo[t] == 'L':
        d -= 1
    if turninfo[t] == 'D':
        d += 1
    if d == -1:
        d = 3
    if d == 4:
        d = 0
x, y = 0, 0  # 첫 시작 좌표는
body[x][y] = 1  # 뱀의 위치한 좌표를 확인할 수 있는 그래프/ 뱀이 있으면 1, 뱀이 없으면 0
snake = deque()  # 뱀이 위치한 좌표를 담은 큐
snake.append((0, 0))
while True:
    t += 1
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <=nx < n and 0 <= ny < n and body[nx][ny] == 0:
        body[nx][ny] = 1
        snake.append((nx, ny))
        if (nx, ny) in apple:
            apple.remove((nx, ny))
        else:
            tail_x, tail_y = snake.popleft()
            body[tail_x][tail_y] = 0
    else:
        print(t)
        break
    x = nx
    y = ny
    if t in turninfo:
        turn(t)