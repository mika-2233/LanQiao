def main():
    n = int(input())
    d = []
    for _ in range(n):
        a, b, g, k = map(int, input().split())
        d.append([a, b, g, k])
    x, y = map(int, input().split())

    # 由于遍历每一个点会超空间 所以我们之遍历每一个地毯
    # 并在每一次遍历的时候判断是否覆盖指定点
    ans = -1
    for i in range(n):
        if (
            (x >= d[i][0] and x <= d[i][0] + d[i][2])
            and y >= d[i][1]
            and y <= d[i][1] + d[i][3]
        ):
            ans = i + 1
    if ans == -1:
        print(ans)
        return
    print(ans)
    return


if __name__ == "__main__":
    main()
