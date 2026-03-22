import math

n=int(input())
answer=0

for _ in range(n):
    a,t=input().split()
    a=float(a)
    t=int(t)
    for i in range(1,t+1):
        x=math.floor(a*i) # 操作的灯的编号
        answer^=x
print(answer)