n=int(input())
l=list(map(int,input().split()))

if all(c == 0 for c in l):
    print("0")
    exit()

result = []
for i, c in enumerate(l):
    exp = n - i
    
    if c == 0:
        continue
    
    if c > 0:
        sign = "+" if result else ""
    else:
        sign = "-"
        c = -c  # 取绝对值
    
    if exp == 0:
        term = str(c)
    elif exp == 1:
        term = "x" if c == 1 else f"{c}x"
    else:
        term = "x^{}".format(exp) if c == 1 else f"{c}x^{exp}"
    
    result.append(sign + term)

print("".join(result))

# if l[0]<-1:
#     s=f'{l[0]}x^{n}'
# elif l[0]==0:
#     s=f''
# elif l[0]==1:
#     s=f'x^{n}'
# elif l[0]==-1:
#     s=f'-x^{n}'
# else:
#     s=f'{l[0]}x^{n}'
# n-=1

# for i in range()

# for i in l[1:-1]:
#     if i<-1:
#         s+=f'{i}x^{n}'
#     elif i==0:
#         pass
#     elif i==1:
#         s+=f'+x^{n}'
#     elif i==-1:
#         s+=f'-x^{n}'
#     else:
#         s+=f'+{i}x^{n}'
#     n-=1

# if l[-1]<-1:
#     s+=f'{l[-1]}'
# elif l[-1]==0:
#     pass
# elif l[-1]==1:
#     s+=f'+1'
# elif l[-1]==-1:
#     s+=f'-1'
# else:
#     s+=f'+{l[-1]}'
# print(s)