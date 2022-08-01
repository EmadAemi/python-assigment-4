def chess(n, m):
    for i in range(n):
        if i % 2 != 0: print("#", end='')
        for j in range(m - i % 2):
            if j % 2 == 0: print("*", end='')
            else: print("#", end='')
        print("")


chess(int(input("N: ")), int(input("M: ")))
