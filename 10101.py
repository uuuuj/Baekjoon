import sys
angle = []
for i in range(3):
    angle.append(int(sys.stdin.readline()))
hap = 0
equal = []
for i in range(3):
    hap += angle[i]

if angle.count(60) == 3:
    print("Equilateral")
else:
    if hap == 180:
        for i in range(len(angle)):
            if angle.count(angle[i]) == 2:
                equal.append(angle[i])
                break
        if len(equal) >= 1:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Error")


