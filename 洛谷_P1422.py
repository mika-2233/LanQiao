a=int(input())
sum=0

if a>=401:
    sum+=(a-400)*0.5663
    a=400
if a>=151:
    sum+=(a-150)*0.4663
    a=150
if a>0:
    sum+=a*0.4463
print(f'{sum:.1f}')