n,d=map(int,input().split())

inp=list(map(int,input().split()))
inp_sor=sorted(inp,key=lambda x:x)
del inp
# print(inp_sor)

count=0
for i in range(n):
    l=inp_sor[i]
    for j in range(i+1,n):
        r=inp_sor[j]
        if r-l<=d:
            count+=1
        else:
            break

print(count)