def main():
    n, m, p = map(int, input().split())

    f = list(range(n + 1))  # 初始化并查集

    def find(x):  # 路径压缩
        if f[x] != x:
            f[x] = find(f[x])
        return f[x]

    def union(x, y):  # 合并列表
        rx = find(x)
        ry = find(y)  # 找到根节点
        if rx != ry:  # 如果根节点不同就合并
            f[rx] = ry
        return

    for i in range(m):
        a, b = map(int, input().split())
        union(a, b)

    res = []
    for k in range(p):
        x, y = map(int, input().split())
        rx = find(x)
        ry = find(y)
        if rx == ry:
            res.append("Yes")
        else:
            res.append("No")

    for j in res:
        print(j)
    return


if __name__ == "__main__":
    main()
