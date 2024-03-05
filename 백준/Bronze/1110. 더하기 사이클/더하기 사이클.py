N = int(input())
hap = (N // 10) + (N % 10)
new = int(str(N%10) + str(hap % 10))

cnt = 1
while new != N:
    hap = (new // 10) + (new % 10)
    new = int(str(new % 10) + str(hap % 10))
    cnt += 1

print(cnt)