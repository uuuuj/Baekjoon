S = input().upper()
uniq = list(set(S))
cnt_list = []
for x in uniq:
    cnt = S.count(x)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(uniq[max_index])



