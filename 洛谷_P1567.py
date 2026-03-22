n=int(input())
l=list(map(int,input().split()))

ll=[]
count=0
a=l[0]
for i in range(1,n):
    if l[i]>a:
        count+=1
        a=l[i]
    else:
        # print(count)
        ll.append(count)
        count=1
        a=l[i]
ll.append(count)
# print(ll)
print(max(ll))