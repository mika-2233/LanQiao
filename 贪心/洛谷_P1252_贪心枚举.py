minn=1145141919810 #一直错的原因是minn设置太小了 原本为114514 测试例最大10^7 shit
ans=0
tag=-1
a=[]
c=[1]*5 # 每个人都要上场所以至少跑了一公里

for i in range(5):
    line=list(map(int,input().split()))
    a.append(line)

for i in range(20): # 每个人初始跑了一公里 所以25-5=20
    minn=1145141919810
    tag=-1
    for j in range(5):
        if c[j]<10:
            cost = a[j][c[j]]-a[j][c[j]-1]
            if cost<minn:
                tag=j
                minn=cost
    if tag==-1:
        break
    c[tag]+=1

for i in range(5):
    ans+=a[i][c[i]-1]

print(ans)
print(f'{c[0]} {c[1]} {c[2]} {c[3]} {c[4]}')