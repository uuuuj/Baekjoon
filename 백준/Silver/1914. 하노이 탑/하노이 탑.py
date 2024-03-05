#n : 원반 개수, a: 시작, b: 보조, c:목표
import sys

cnt = 0
def hanoi(n, a, c, b):
    global cnt
    if n == 1:
        print(a, c)
        cnt += 1
        return
    hanoi(n-1, a, b, c)
    print(a, c)
    cnt += 1
    hanoi(n-1, b, c, a)

n = int(sys.stdin.readline())

if n <= 20:
    print(2 ** n - 1)
    hanoi(n, 1, 3, 2)
else:
    print(2 ** n -1)
