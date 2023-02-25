num = [0] * (10)
nam = [0] * (10)
result = []
for n in range(10):
    num[n] = int(input())
    nam[n] = num[n] % 42
for value in nam:
    if value not in result:
        result.append(value)

print(len(result))