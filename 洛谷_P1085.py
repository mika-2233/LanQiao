m=8
day=0

for i in range(1,8):
    cl,ou=map(int,input().split())
    if m<cl+ou:
        m=cl+ou
        day=i
print(day)