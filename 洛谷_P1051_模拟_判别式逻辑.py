n=int(input())

Sum=0
local_max=0
a1,a2,a3,a4,a5=0,0,0,0,0
for _ in range(n):
    name,gradeA,gradeB,g,k,l=input().split()
    gradeA,gradeB,l=int(gradeA),int(gradeB),int(l)
    if gradeA>80 and l>=1:
        a1=1
    if gradeA>85 and gradeB>80:
        a2=1
    if gradeA>90:
        a3=1
    if gradeA>85 and k=='Y':
        a4=1
    if gradeB>80 and g=='Y':
        a5=1
    sum=(a1*8000)+(a2*4000)+(a3*2000)+(a4*1000)+(a5*850)
    Sum+=sum
    a1,a2,a3,a4,a5=0,0,0,0,0
    if sum>local_max:
        local_max=sum
        ans_name=name
    # print(f'name:{name}, sum:{sum}, ans_name:{ans_name}, local_max:{local_max}')
print(ans_name)
print(local_max)
print(Sum)