#소수 판별 함수 생성
import sys


def is_sosu(i):
    if i == 1:
        return False
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            return False
    return True
#테스트 케이스 수와 짝수 입력
T = int(sys.stdin.readline())

for i in range(T):
    num = int(sys.stdin.readline())
    #주어진 짝수의 중간 수를 두개의 변수로 저장
    A = num // 2
    B = num // 2
    #0~중간 수 까지 소수 함수에 대입
    for j in range(A):
        if is_sosu(A) and is_sosu(B):
            print(A, B)
            break
        else:
            A -= 1
            B += 1
#소수이면 출력, 아니면 두 수를 하나씩 더해주고 빼기