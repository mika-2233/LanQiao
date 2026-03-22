n=int(input())
minn=1145141919
for i in range(3):
    a,b=map(int,input().split())
    # 只买同一种包装
    if n%a==0: # 包装正好满足倍数
        minn=min(minn,n//a*b)
    else: # 如果不满足那就再买一盒
        minn=min(minn,(n//a+1)*b)
print(minn)


