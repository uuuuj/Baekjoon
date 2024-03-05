import sys
table = []
n = int(sys.stdin.readline())
for i in range(n):
    st, en = map(int, sys.stdin.readline().split())
    table.append([st, en])

table.sort(key=lambda x:(x[1], x[0]))
end = table[0][1]

cnt = 1
for i in range(1, n):
    if table[i][0] >= end:
        cnt += 1
        end = table[i][1]
print(cnt)