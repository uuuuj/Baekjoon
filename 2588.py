A = int(input())
B = int(input())

#세자리 자연수로 고정
num_1 = B//100 #100의 자리 수
num_2 = (B%100)//10 #10의 자리 수
num_3 = (B%100)%10 #1의 자리 수

print(A * num_3)
print(A * num_2)
print(A * num_1)
print((A*num_1)*100 + (A*num_2)*10 + (A*num_3))
