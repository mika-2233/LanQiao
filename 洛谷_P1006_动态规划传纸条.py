# def FourDimensions_DP(m,n,matrix):
#     # 初始化array
#     a = [[0]*(n+1) for _ in range(m+1)] # 创建一个m+1行n+1列的二维列表 保留边界以便计算
#     dp = [[[[0]*(n+1) for _ in range(m+1)] for _ in range(n+1)] for _ in range(m+1)]

#     # 插入数据
#     for i in range(1, m+1): # 从1开始在m结束是为了构建边界
#         for j in range(1, n+1): # 同理
#             a[i][j] = matrix[i-1][j-1]

#     # 四维动态规划
#     # 分为两个路径 向右下走的用i和j描述 向左上走的用k和l描述
#     # 为什么不反向遍历k和l呢 因为路径实际上是可逆的 方向并不重要 只需要保证两个路径不重叠即可
#     for i in range(1, m+1):
#         for j in range(1, n+1):
#             for k in range(1, m+1):
#                 for l in range(1, n+1):
#                     # 右下路径：从上方向下 上方权重为i-1
#                     # 左上路径：从下方向上 下方权重为k-1 或者 从右往左 右侧权重为l-1
#                     dp[i][j][k][l] = max(dp[i-1][j][k-1][l], dp[i-1][j][k][l-1])
#                     # 合并上一行对dp的定义
#                     # 右下路径：从左方向右 左方权重为j-1
#                     # 左上路径：从下方向上 下方权重为k-1 或者 从右往左 右侧权重为l-1
#                     dp[i][j][k][l] = max(dp[i][j-1][k-1][l], dp[i][j-1][k][l-1], dp[i][j][k][l])
#                     # 加上当前所在点的权重
#                     dp[i][j][k][l] += a[i][j] + a[k][l]
#                     if (i==k and j==l and not ((i==1 and j==1) or (i==m and j==n))):
#                         # 如果当前两条路径没有在除了终点和起点的位置重合 那么将当前路径的权重设置为-2333
#                         # 即：将这个路径设置为非法
#                         dp[i][j][k][l] = -2333
#     return dp[m][n][m][n]

# m,n = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(m)]
# result = FourDimensions_DP(m,n,matrix)
# print(result)

# 上面的四维动态规划虽然直观 但是提交后超出内存和时间限制 优化为三维更佳

def Four_To_ThreeDimensions_DP(m,n,matrix):
    a = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            a[i][j] = matrix[i-1][j-1]

    # 由于两条路径在规划的时候步长是相同的i + j == k + l 所以可以设s = i + j = k + l
    # 所以只需枚举 s, i, k，j = s - i，l = s - k 自动确定
    # 构建三维数组dp[s][i][k]
    total_steps = m+n
    dp = [[[0]* (m+1) for _ in range(m+1)] for _ in range(total_steps+1)]
    # 确定dp初始状态
    dp[2][1][1] = a[1][1]

    for s in range(3, total_steps+1): # 由于s=2也就是起点已经初始化 所以从3开始
        for i in range(1, min(s, m+1)):
            j = s-i
            if j<1 or j>n:
                continue
            for k in range(1, min(s, m+1)):
                l = s-k
                if l<1 or l>n:
                    continue
                
                candidates = [
                    dp[s-1][i-1][k-1], # 两条路径都向下
                    dp[s-1][i-1][k], # 一条向下 另一条向右
                    dp[s-1][i][k-1], # 一条向右 另一条向下
                    dp[s-1][i][k] # 两条都向右
                ]
                dp[s][i][k] = max(candidates)
                dp[s][i][k] += a[i][j] + a[k][l]
                if (i==k and j==l and not ((i==1 and j==1) or (i==m and j==n))):
                    dp[s][i][k] = -2333
    return dp[total_steps][m][m]

m,n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
result = Four_To_ThreeDimensions_DP(m,n,matrix)
print(result)

'''
3 3
0 3 9
2 8 5
5 7 0

初始化结果
3 3
[[0, 3, 9], [2, 8, 5], [5, 7, 0]]
'''