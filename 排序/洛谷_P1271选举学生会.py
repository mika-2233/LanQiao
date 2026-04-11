n,m=map(int,input().split())

inp=list(map(int,input().split()))
# print(inp)
inp_sor=sorted(inp,key=lambda x:x)
# print(inp_sor)
del inp
str_inp_sor=list(map(str,inp_sor))
print(" ".join(str_inp_sor))