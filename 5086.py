while True:
    try:
        N, M = map(int, input().split())
        if N < M:
            if M % N == 0:
                print("factor")
            else:
                print("neither")
        elif N > M:
            if N % M == 0:
                print("multiple")
            else:
                print("neither")
    except EOFError:
        break