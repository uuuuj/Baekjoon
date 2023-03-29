while True:
    hap = 0
    yak = []
    n = int(input())
    if n == -1:
        break
    else:

        for i in range(1, n):
            if n % i == 0:
                yak.append(i)
            else:
                pass
            yak.sort()

        for j in range(0, len(yak)):
            hap += yak[j]

        if hap == n:
            print(n, "=", end=" ")
            for k in range(0, len(yak)):
                print(yak[k], end="")
                if yak[k] != yak[-1]:
                    print(" +", end=" ")
                else:
                    print('')
        else:
            print(n, "is NOT perfect.")

