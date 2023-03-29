word = []
length = []
for i in range(5):
    word.append(list(input()))
    length.append(len(word[i]))
max_len = max(length)
for i in range(5):
    if len(word[i]) < max_len:
        for j in range(len(word[i])-1, max_len-1):
            word[i].append("")
    else:
        pass
for i in range(max_len):
    for j in range(5):
        print(word[j][i], end='')
