import sys

N = int(sys.stdin.readline())
sang_card_list = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
check_card_list = list(map(int, sys.stdin.readline().split()))

for i in range(len(check_card_list)):
    low, high = 0, N-1
    exist = False
    while low <= high:
        mid = (low+high)//2
        if check_card_list[i] < sang_card_list[mid]:
            high = mid - 1
        elif check_card_list[i] > sang_card_list[mid]:
            low = mid + 1
        else:
            exist = True
            break
    print(1 if exist else 0, end=' ')



