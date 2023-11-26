N = int(input())
text = input()
sum_num = 0
current_num = ''

for char in text:
    if char.isdigit():
        current_num += char
    elif current_num:
        sum_num += int(current_num)
        current_num = ''

if current_num:
    sum_num += int(current_num)

print(sum_num)
