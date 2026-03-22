l=list(map(int,input().split()))
n=l[0]
a=[0]*(n*n+2)
count=1
i=1
index=1
while index<len(l):
    x=l[index]
    index+=1
    if count%2!=0:
        i+=x
    else:
        for _ in range(x):
            a[i]=1
            i+=1
    count+=1

for i in range(1,n*n+1):
    print(a[i],end='')
    if i%n==0:
        print()