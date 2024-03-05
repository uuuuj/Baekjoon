import sys

A, B, V = map(int, sys.stdin.readline().split())

V_minus_B = V - B

if V <= A:
    print(1)

else:
    if V_minus_B % (A-B) == 0:
        print((V_minus_B // (A - B)))
    else:
        print((V_minus_B // (A - B))+1)







