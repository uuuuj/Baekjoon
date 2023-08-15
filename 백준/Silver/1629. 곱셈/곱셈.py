import sys


def power(a, b, c):
    if b == 1:
        return a % c
    if b % 2 == 0:
        return (power(a, b//2, c) ** 2) % c
    else:
        return ((power(a, b//2, c) ** 2)* a) % c

A, B, C = map(int, sys.stdin.readline().split())



print(power(A, B, C))