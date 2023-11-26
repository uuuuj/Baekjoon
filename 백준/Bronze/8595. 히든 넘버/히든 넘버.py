N = int(input())
text = input()

sum_num = 0
hidden_num = ''

for word in text:
    if word.isdigit():
        hidden_num += word
    elif hidden_num:
        sum_num += int(hidden_num)
        hidden_num = ''
if hidden_num:
    sum_num += int(hidden_num)

print(sum_num)