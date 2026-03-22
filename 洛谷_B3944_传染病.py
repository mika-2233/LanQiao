'''
k,a,q=map(int,input().split())
mod=722733748
ans=1
for i in range(1,k+1):
    ans*=a%mod # 当前的感染人数
    a*=q%mod # 下一天的感染人数
print(ans%mod)

以上代码超时
优化方法过于复杂 故跳过
'''
