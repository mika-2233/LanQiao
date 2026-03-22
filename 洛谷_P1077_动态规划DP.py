n,m = map(int,input().split())

l=input().strip()
a=list(map(int,l.split()))
mod = 1000007

# dp[i][j]=在摆j盆花下 摆前i种花 的方案数
dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1 # 不论有多少种花 只要不摆就算一个方案
for i in range(1,n+1):
    for j in range(m+1):
        total = 0
        for k in range(0,min(a[i-1],j)+1):
            add = dp[i-1][j-k]
            total+=add
            dp[i][j] = total % mod
print(dp[n][m])