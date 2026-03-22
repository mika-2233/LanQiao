tt, m = map(int, input().split()) # 70 3

time_l = [] #  [71, 69, 1]
value_l = [] # [100, 1, 2]
for _ in range(m):
    line = input().strip()
    if line:
        t, v = map(int, line.split())
        time_l.append(t)
        value_l.append(v)

# dp[i][j]=当总的可采摘时间为j时，有i种草药可以采(1代表只能采1号 2代表能采1,2...) 采得的价值
# 这实际上是背包DP 只是换了变量名
dp = [[0]* (tt+1) for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(tt+1):
        if j>=time_l[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time_l[i-1]]+value_l[i-1])
            # dp[i][j] = max(不选当前草药, 选当前草药)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[m][tt])