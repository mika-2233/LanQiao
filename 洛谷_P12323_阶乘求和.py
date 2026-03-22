# 1!+2!+3!+4!+5!=1+2+6+24+120=153
# a=0
# b=1
# for i in range(1,40):
#   b=b*(i+1)
# print(b)
# 815915283247897734345611269596115894272000000000 当阶乘到40时，0的个数将达到9个
# 利用这个特性 我们只需要计算前39个阶乘的和
mod=10**9
ans=0
for i in range(1,39):
    a=1
    for j in range(1,i+1):
        a*=(j+1)
        a=a%mod
    ans+=a
    ans=ans%mod
print(ans+1)
