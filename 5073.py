import copy
import sys
coord = []
while True:
    x, y, z = map(int, sys.stdin.readline().split())
    coord.append(x)
    coord.append(y)
    coord.append(z)
    coord1 = copy.deepcopy(coord)
    max_co = max(coord1)
    ind = coord.index(max_co)
    del coord1[ind]

    if x == 0 and y == 0 and z == 0:
        break
    else:
        if max_co >= coord1[0] + coord1[1]:
            print("Invalid")
        else:
            if coord.count(coord[0]) == 3 or coord.count(coord[1]) == 3 or coord.count(coord[2]) == 3:
                print("Equilateral")

            elif coord.count(coord[0]) == 2 or coord.count(coord[1]) == 2 or coord.count(coord[2]) == 2:
                print("Isosceles")

            else:
                print("Scalene")

    coord = []