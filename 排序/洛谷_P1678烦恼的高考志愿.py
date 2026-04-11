m,n=map(int,input().split())

yujiluqu=list(map(int,input().split()))
estimate=list(map(int,input().split()))

yujiluquSor=sorted(yujiluqu,key=lambda x:x)
del yujiluqu

ans=0
for i in range(n):
    l=0
    r=m
    while l<r:
        mid=(l+r)//2
        # print(mid)
        if yujiluquSor[mid]<=estimate[i]:
            l=mid+1
        else:
            r=mid
    
    if l == 0:
        ans += yujiluquSor[0] - estimate[i]
    elif l == m:
        ans += estimate[i] - yujiluquSor[m-1]
    else:
        ans+=min(abs(yujiluquSor[l-1]-estimate[i]),abs(yujiluquSor[l]-estimate[i]))

print(ans)