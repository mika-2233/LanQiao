# 如果两个数的异或为1，那么这两个数的差一定也为一
# 所以这两个数一定是相邻的奇数和偶数
# 而只有第一个质数2是偶数，所以只有当x=1且y=2或者相反的时候答案为Yes
t = int(input())
res = [0] * t
for _ in range(t):
    a, b = map(int, input().split())
    if a == 1 and b == 2:
        res[_] = True
    elif a == 2 and b == 1:
        res[_] = True
    else:
        continue
for i in range(t):
    if res[i]:
        print("Yes")
    else:
        print("No")
