A, B = input().split()
# print(A)
# print(B)
# breakpoint()
A_list = list(A)
B_list = list(B)
#리스트 역순으로
A_list.reverse()
B_list.reverse()
#리스트 문자열로
A2 = ''.join(A_list)
B2 = ''.join(B_list)

A3 = int(A2)
B3 = int(B2)

if A3 > B3:
    print(A3)
else:
    print(B3)