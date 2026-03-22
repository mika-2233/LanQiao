v = int(input())
n = int(input())

v_l = []
for _ in range(n):
    line = int(input().strip())
    v_l.append(line)

# dp[i][j]=当容量为j时，装入i个物品 利用的最大空间
dp = [[0]*(v+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, v+1):
        if j >= v_l[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-v_l[i-1]]+v_l[i-1])
        else:
            dp[i][j] = dp[i-1][j]
print(v-dp[n][v]) # 总空间减去最大空间就是剩余的最小空间