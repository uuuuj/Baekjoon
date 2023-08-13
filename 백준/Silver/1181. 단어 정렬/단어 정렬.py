import sys
#중복 제거
string = set(sys.stdin.readline().strip() for i in range(int(sys.stdin.readline())))
#사전 순 정렬
string = sorted(string)
#길이 순 정렬
string = sorted(string, key=lambda x : len(x))
for i in string:
    print(i)