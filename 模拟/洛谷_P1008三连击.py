d = [0] * 9
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            a = i * 100 + j * 10 + k

            b = a * 2
            b1 = b // 100
            b2 = (b % 100) // 10
            b3 = b % 10

            c = a * 3
            c1 = c // 100
            c2 = (c % 100) // 10
            c3 = c % 10

            d[0] = i
            d[1] = j
            d[2] = k
            d[3] = b1
            d[4] = b2
            d[5] = b3
            d[6] = c1
            d[7] = c2
            d[8] = c3
            flag = 0
            for m in range(9):
                for n in range(m + 1, 9):
                    if d[m] == d[n]:
                        flag = 1
            # 如果c小于999 且两个乘出来的数中没有0
            if not flag and c <= 999 and b2 and c2 and b3 and c3:
                print(f"{a} {b} {c}")
