import sys


def main():
    res = []
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        parts = list(map(int, line.split()))
        if len(parts) == 1 and parts[0] == 0:
            break
        n, m = parts

        # 初始化并查集
        parent = list(range(n + 1))

        def find(x):  # 找到当前节点的祖先
            if parent[x] != x:  # 路径压缩
                parent[x] = find(parent[x])  # 每个孩子指向最高的祖先
            return parent[x]

        def union(x, y):  # 合并两个集合
            root_x = find(x)
            root_y = find(y)  # 找出祖先同时路径压缩
            if root_x != root_y:  # 如果两个集合的祖先不同
                parent[root_x] = root_y  # 那么将x的祖先节点的祖先修改为y节点的祖先
            return

        # 读入 m 条边
        for _ in range(m):
            u, v = map(int, sys.stdin.readline().split())
            union(u, v)

        # 统计连通块数量
        components = 0
        for i in range(1, n + 1):
            if find(i) == i:
                components += 1  # 找到一个根节点计数+1 代表找到一个连通块
        res.append(components - 1)  # 连通块之间需要计数-1条道路连通

    for i in res:
        print(i)
    return


if __name__ == "__main__":
    main()
