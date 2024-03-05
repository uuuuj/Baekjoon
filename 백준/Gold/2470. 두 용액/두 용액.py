import sys

N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))

st = 0
en = N - 1
ans = abs(arr[st] + arr[en])
final = [arr[st], arr[en]]

while st < en:
    left = arr[st]
    right = arr[en]

    sum = left + right
    if abs(sum) < ans:
        ans = abs(sum)
        final = [left, right]
        if ans == 0:
            break
    if sum < 0:
        st += 1
    else:
        en -= 1

print(final[0], final[1])