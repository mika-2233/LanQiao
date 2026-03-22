n = int(input())
inp = list(map(int, input().split()))

maxx = minn = inp[0]
m = inp[0]
i = 1
for x in range(1, n):
    xx = inp[x]
    if xx > maxx:
        maxx = xx
    elif xx < minn:
        minn = xx
    m += xx
    i += 1
    if i >= 3:
        localm = m
        localm = localm - (maxx + minn)
        ans = float(localm / (i - 2))
        print(f"{ans:.2f}")
