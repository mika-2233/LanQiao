n,k=map(int,input().split())
a=n
sum=n

while a>=k:
    a-=k
    sum+=1
    a+=1
print(sum)

# 方法超时
# while n>0:
#     n-=1
#     a+=1
#     ans+=1
#     if a==k:
#         a=0
#         n+=1
# print(ans)
