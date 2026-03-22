def main():
    n, m = map(int, input().split())
    f = [list(input().strip()) for _ in range(n)]

    ans = 0
    count = []
    for i in range(n):
        numW = numB = numR = 0
        for j in range(m):
            if f[i][j] == "W":
                numW += 1
            elif f[i][j] == "B":
                numB += 1
            else:
                numR += 1
        # 每一行统计三个颜色的数量并计入
        count.append([numW, numB, numR])
    # 既然最上方行是白色的，那么第一行就一定是白色
    # 既然剩下的行都要是红色的，那么最后一行就一定是红色
    first = m - count[0][0]
    last = m - count[n - 1][2]
    ans += first + last
    # print(f"第一行涂{first}格，最后一行行涂{last}格，当前ans: {ans}")

    # 暴力计算除了第一行最后一行分别换成三种颜色的成本
    cosW = []
    cosB = []
    cosR = []
    for i in range(1, n - 1):
        cosW.append(m - count[i][0])
        cosB.append(m - count[i][1])
        cosR.append(m - count[i][2])
    print(cosW)
    print(cosB)
    print(cosR)
    minn = 114514
    for i in range(len(cosW) - 1):
        for j in range(i + 1, len(cosW)):
            w = cosW[i]
            b = cosB[j]
            if w + b < minn:
                minn = w + b
                indexi = i + 1
                indexj = j + 1
                print(f"找到更小：{w + b}，索引i: {i}, j: {j}")

    print(f"i: {indexi}, j: {indexj}")

    """
    # 找出存在B最多的行并涂成B
    maxB = index = 0
    for i in range(1, n - 1):
        if count[i][1] > maxB:
            maxB = count[i][1]
            index = i
    ans += m - maxB
    # print(f"行{index}涂为B，涂{m - maxB}格，当前ans: {ans}")

    # 在B行上面的行判断B和W哪个多
    for i in range(1, index):
        maxWB = max(count[i][0], count[i][1])
        ans += m - maxWB
        # print(f"行{i}涂成W，涂{m - maxWB}格W，当前ans: {ans}")
    # 在B行下判断B和R哪个多
    for i in range(index + 1, n - 1):
        maxBR = max(count[i][1], count[i][2])
        ans += m - maxBR
        # print(f"行{i}涂成R，涂{m - maxBR}格，当前ans: {ans}")
    """

    # print(ans)
    return


# BUG:算法逻辑错误 不符合贪心策略 在一些情况下无法得出最优解
# if __name__ == "__main__":
#     main()

N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]

# 预处理每行变成W/B/R的成本
cost = [[0] * 3 for _ in range(N)]

for i in range(N):
    row = grid[i]
    w_cost = sum(1 for c in row if c != "W")
    b_cost = sum(1 for c in row if c != "B")
    r_cost = sum(1 for c in row if c != "R")
    cost[i][0] = w_cost
    cost[i][1] = b_cost
    cost[i][2] = r_cost

min_changes = 114514

# 枚举W段结束行i，B段结束行j
for i in range(0, N - 2):  # W段: 0..i, 至少留2行给B和R
    for j in range(i + 1, N - 1):  # B段: i+1..j, 至少留1行给R
        total = 0
        # W段
        for k in range(0, i + 1):
            total += cost[k][0]
        # B段
        for k in range(i + 1, j + 1):
            total += cost[k][1]
        # R段
        for k in range(j + 1, N):
            total += cost[k][2]

        if total < min_changes:
            min_changes = total

print(min_changes)
