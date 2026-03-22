def main():
    n, m = map(int, input().split())

    f = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(m):  # 遍历每一个点作为左上角(n,m)为当前的坐标
            max_possibel_k = min(n - i, m - j)  # 即将遍历的正方形的最大高或者宽度
            start_k = min(max_possibel_k, min(n, m))  # 再取一次防止出界
            for k in range(start_k, ans, -1):
                """
                k=正方形的边长 遍历从大到小 尝试所允许的最大边长
                利用了反向for函数的特性 当ans(当前最大正方形)大于允许边长的时候
                for函数将直接跳出
                """
                p = True
                # 逐个判断正方形内是否全为1
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        if f[x][y] == 0:
                            p = False  # 如果当前点等于0 将p标记为False 并跳出当前行的遍历
                            break
                    if (
                        not p
                    ):  # 当行遍历跳出的时候接收p的False并跳出这个正方形的遍历 回到k循环
                        break
                if p:  # 当整个循环结束 说明找到了比当前ans更大的正方形 更新ans 跳出k循环 回到x,y循环 尝试下一个点
                    ans = k
                    break
    print(ans)
    return


if __name__ == "__main__":
    main()
