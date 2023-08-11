import sys

C = int(sys.stdin.readline())
ratio_list = []
for i in range(C):
    cnt = 0
    score = list(map(int, sys.stdin.readline().split()))
    # 학생의 수 n
    n = score[0]
    hap = sum(score[1:])
    avg = hap / n
    for j in score[1:]:
        if j > avg:
            cnt += 1

    ratio = round((cnt / n)*100, 3)
    ratio_list.append(ratio)

for i in ratio_list:
    print(f'{i:.3f}' + '%')
