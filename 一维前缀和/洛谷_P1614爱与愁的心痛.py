def main():
    n, m = map(int, input().split())
    if n == 0:
        print(0)
        return
    inp = []
    for _ in range(n):
        inp.append(int(input()))
    # print(inp)
    # [1, 4, 7, 3, 1, 2, 4, 3]

    # 计算列表前缀和
    for i in range(1, n):
        inp[i] = inp[i - 1] + inp[i]
    # print(inp)
    # [1, 5, 12, 15, 16, 18, 22, 25]

    ans = 1145141919810
    for i in range(m - 1, n):
        b = inp[i - m]
        if i == m - 1:
            b = 0
        ans = min(ans, inp[i] - b)
    print(ans)
    return


if __name__ == "__main__":
    main()
