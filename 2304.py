import sys

N = int(sys.stdin.readline())
coord = []
for i in range(N):
    coord.append(list(map(int, sys.stdin.readline().split())))

coord.sort() #x좌표 오름차순 정렬

space = coord[0][1] #초기 넓이

for i in range(N):
    if coord[i][1] <= coord[i+1][1]:


