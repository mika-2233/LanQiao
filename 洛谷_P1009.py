a = 0
n = int(input())

for i in range(1, n+1):
    i_ = i
    while i>1:
        i_ = i_ * (i-1)
        i-=1
    a += i_
print(a)