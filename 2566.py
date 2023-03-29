A = []
max1 = []
ind_x = []
ind_y = []
for i in range(9):
    A.append(list(map(int, input().split())))

for i in range(9):
    max1.append(max(A[i]))
    ind_x.append((A[i].index(max1[i]))+1)
    ind_y.append(i+1)
result = max(max1)
i = max1.index(result)
print(result)
print(ind_y[i], ind_x[i])