n = int(input())
l = [1]*(n+1)

# 动态规划 dp[i]=数字i对应的合法数列数
for i in range(1, n+1):
    for j in range(1, i//2+1): # 从1到数字i的一半（奇数即为小于一半的最大整数）
        l[i] += l[j]

print(l[n])