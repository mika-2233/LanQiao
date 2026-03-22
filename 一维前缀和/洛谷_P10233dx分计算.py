"""
P 可得 3 分 dx 分。
p 可得 2 分 dx 分。
G 可得 1 分 dx 分。
g 不能得到 dx 分。
m 不能得到 dx 分。
"""


def main():
    # 判别的组数
    t = int(input())
    tlist = [0] * t
    result = []
    for _ in range(t):
        tlist[_] = list(input())
        # 赋分
        for n in range(len(tlist[_])):
            local = tlist[_][n]
            if local == "P":
                tlist[_][n] = 3
            elif local == "p":
                tlist[_][n] = 2
            elif local == "G":
                tlist[_][n] = 1
            else:
                tlist[_][n] = 0
        # print(tlist)
        # 计算前缀和
        for i in range(1, len(tlist[_])):
            tlist[_][i] = tlist[_][i - 1] + tlist[_][i]
        # print(tlist)
        # [[3, 5, 6, 6, 6], [3, 6, 8, 10, 11, 12, 12, 12]]

        # 判别范围输入行数
        num = int(input())
        for k in range(num):
            a, b = map(int, input().split())
            if a == 1:
                result.append(tlist[_][b - 1])
                continue
            result.append(tlist[_][b - 1] - tlist[_][a - 2])
        # print(result)

    for x in result:
        print(x)
    return


# 代码超时 其实也没啥优化空间了
if __name__ == "__main__":
    main()
