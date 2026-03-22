a,b=map(int,input().split())
c=a**b
d=c%7
if d==0:
    print("Sunday")
elif d==1:
    print("Monday")
elif d==2:
    print("Tuesday")
elif d==3:
    print("Wednesday")
elif d==4:
    print("Thursday")
elif d==5:
    print("Friday")
elif d==6:
    print("Saturday")