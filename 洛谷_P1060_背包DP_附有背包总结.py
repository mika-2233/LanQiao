n, m = map(int, input().split())

cost = []
impor = []
for _ in range(m):
    v, p = map(int, input().split())
    cost.append(v)
    impor.append(p)

# dp[i][j]=购买前i个物品所花费的预算j 所获得的最大乘积
dp = [[0]*(n+1) for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(n+1):
        if j>=cost[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i-1]]+(cost[i-1]*impor[i-1]))
        else:
            dp[i][j] = dp[i-1][j]
print(dp[m][n])

'''
无优化背包
for(int i=1;i<=n;i++)
{
    for(int c=0;c<=m;c++)
    {
        f[i][c]=f[i-1][c];
        if(c>=w[i])
        f[i][c]=max(f[i][c],f[i-1][c-w[i]]+v[i]);
    }
}

一维数组优化
for(int i=1;i<=n;i++)
{
    for(int c=m;c>=0;c--)
    {
        if(c>=w[i])
        f[c]=max(f[c],f[c-w[i]]+v[i]);
    }
}

常数优化背包
for(int i=1;i<=n;i++)
{
    sumw+=w[i];
    bound=max(m-sumw,w[i]);
    for(int c=m;c>=bound;c--)
    {
        if(c>=w[i])
        f[c]=max(f[c],f[c-w[i]]+v[i]);
    }
}

完全背包问题
for(int i=1;i<=n;i++)
{
    for(int c=0;c<=m;c++)
    {
        if(c>=w[i])
        f[c]=max(f[c],f[c-w[i]]+v[i]);
    }
}

多重背包问题
for(int i=1;i<=n;i++)
{
    if(w[i]*a[i]>m)
    {
        for(int c=0;c<=m;c++)
        {
        if(c>=w[i])
        f[c]=max(f[c],f[c-w[i]]+v[i]);
        }
    }
    else
    {
         k=1;amount=a[i];
         while(k<amount)
         {
             for(int c=k*w[i];c>=0;c--)
             {
                 if(c>=w[i])
                 f[c]=max(f[c],f[c-w[i]]+k*v[i]);
             }
             amount-=k;
             k<<=1;
         }  
         for(int c=amount*w[i];c>=0;c--)
         {
             f[c]=max(f[c],f[c-w[i]]+amount*v[i]);
         }
    } 
}
'''