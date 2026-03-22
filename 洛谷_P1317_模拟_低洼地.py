n=int(input())
l=list(map(int,input().split()))

left,right=-1,-1
low=0
ans=0
for i in range(1,len(l)):
    left=l[i-1]
    right=l[i]
    if right<left:
        low=1
    elif right>left and low==1:
        ans+=1
        low=0
print(ans)