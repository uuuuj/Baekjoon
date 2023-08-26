import sys
# -를 기준으로 나눠서 저장
sum = list(sys.stdin.readline().split('-'))
# - 뒤부터 가장 큰 값을 누적합으로 계산해서 가장 큰 부분에 괄호 넣어줌
ans = 0
for i in sum[0].split('+'):
    ans += int(i)
for i in sum[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)