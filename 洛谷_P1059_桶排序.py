n = int(input())
l=list(map(int,input().split()))

m=0
a=[0]*1010
for b in l[:n]:
    a[b]+=1
    if a[b]==1:
        m+=1
print(m)
for i in range(1,1001):
    if a[i]!=0:
        print(i,end=' ')