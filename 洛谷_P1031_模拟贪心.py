n=int(input())
l=list(map(int,input().split()))

target=int(sum(l)/n)
ans=0
for i in range(n):
    if l[i]==target:
        continue
    l[i+1]+=(l[i]-target)
    l[i]=target
    ans+=1
print(ans)