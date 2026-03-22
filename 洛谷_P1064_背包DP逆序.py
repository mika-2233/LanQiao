n,m = map(int,input().split())

l=[]
for i in range(m):
    v,p,q = map(int,input().split())
    f1,f2 = -1,-1
    l.append([v,p,q,f1,f2])
for i in range(m):
    if l[i][2]>0: # 如果是附件
        if l[l[i][2]-1][3]==-1: # 如果对应主件槽位1没有附件
            l[l[i][2]-1][3] = i # 那么存入槽位1
        else:
            l[l[i][2]-1][4] = i

# dp[i][j]=花费预算j购买前i件物品 所得到乘积的最大值
# 1.只购买主件
# 2.购买主件和一个附件（选择附件1或2）
# 3.购买主件和两个附件
# 4.什么都不买
# 对于附件 则是继承前i-1件物品的状态
# 由于附件无法单独购买 我们可以在逻辑上将主件和附件处理为同一个物品

# 二维数组超时
# dp = [[0]*(n+1) for _ in range(m+1)]
# for i in range(1, m+1):
#     for j in range(1, n+1):
#         if l[i-1][2]!=0: # 如果当前物品是附件 那么继承状态即可
#             dp[i][j] = dp[i-1][j]
#         else: # 如果是主件
#             v, p = l[i-1][0], l[i-1][1]
#             f1, f2 = l[i-1][3], l[i-1][4]
#             v1, p1 = l[f1][0], l[f1][1]
#             v2, p2 = l[f2][0], l[f2][1]
#             if j>=l[i-1][0]: # 如果预算大于当前主件价格
#                 dp[i][j] = max(dp[i-1][j], dp[i-1][j-l[i-1][0]]+(v*p))
#             if l[i-1][3]>0 and j>=l[i-1][0]+l[l[i-1][3]][0]: # 如果附件1存在且预算足够
#                 dp[i][j] = max(dp[i-1][j], dp[i-1][j-v-v1]+((v*p)+(v1*p1)))
#             if l[i-1][4]>0 and j>=l[i-1][0]+l[l[i-1][4]][0]: # 如果附件2存在且预算足够    
#                 dp[i][j] = max(dp[i-1][j], dp[i-1][j-v-v2]+((v*p)+(v2*p2)))
#             if l[i-1][3]>0 and l[i-1][4]>0 and j>=l[i-1][0]+l[l[i-1][3]][0]+l[l[i-1][4]][0]: # 如果两个附件都存在且预算足够
#                 dp[i][j] = max(dp[i-1][j], dp[i-1][j-v-v1-v2]+((v*p)+(v1*p1))+((v2*p2)))
# print(dp[m][n])

# 一维DP 倒序更新
dp = [0]*(n+1)
for i in range(m):
    if l[i][2] !=0:
        continue # 如果是附件那么跳过
    v0,p0 = l[i][0],l[i][1]
    f1,f2 = l[i][3],l[i][4]
    ll = []
    ll.append((v0,v0*p0))
    if f1!=-1:
        v1,p1 = l[f1][0],l[f1][1]
        ll.append((v0+v1,v0*p0+v1*p1))
    if f2!=-1:
        v2,p2 = l[f2][0],l[f2][1]
        ll.append((v0+v2,v0*p0+v2*p2))
    if f1!=-1 and f2!=-1:
        v1,p1 = l[f1][0],l[f1][1]
        v2,p2 = l[f2][0],l[f2][1]
        ll.append((v0+v1+v2,v0*p0+v1*p1+v2*p2))

    for j in range(n, -1, -1):
        for cost, value in ll:
            if j>=cost:
                if dp[j]<dp[j-cost]+value:
                    dp[j] = dp[j-cost]+value
print(dp[n])