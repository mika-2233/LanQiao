a,b,c,d=map(int,input().split())

k=0
j=0
if b!=0:
    k+=c-(a+1)
    j+=60-b+d
else:
    k+=c-a
    j+=d
if j>=60:
    k+=1
    j-=60
print(f'{k} {j}')