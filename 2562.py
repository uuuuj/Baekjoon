ans = []
for i in range(9):
    ans.append(int(input()))

print(max(ans))
print(ans.index(max(ans)) + 1)