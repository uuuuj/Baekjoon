import sys

N = int(sys.stdin.readline())
#전달인자 x, y : 해당 사분면의 가장 왼쪽 위 좌표
board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
blue = 0
white = 0

def solution(x, y, n):
    global blue, white
    color = board[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != board[i][j]:
                solution(x, y, n//2)
                solution(x, y+(n//2), n//2)
                solution((x+n//2),y,n//2)
                solution(x+(n//2), y+(n//2), n//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

solution(0, 0, N)
print(white)
print(blue)