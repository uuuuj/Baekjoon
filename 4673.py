N = [i for i in range(1, 10001)]
N_set = set(N)
num_list = []
for i in N:
    for n in str(i):
        i += int(n)
    if i <= 10000:
        num_list.append(i)

num_set = set(num_list)
ans_set = N_set - set(num_set)
ans_list = list(ans_set)
ans_list.sort()
##xptmxm
for i in range(len(ans_list)):
    print(ans_list[i])
