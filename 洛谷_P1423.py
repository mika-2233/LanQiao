s=float(input())
n=0.98
a=2
ss=0
count=0

while ss<s:
    ss+=a
    a*=n
    count+=1

print(count)
