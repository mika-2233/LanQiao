"""
res = [0]
res[0] = "1/1"
count = 1
a = 1
b = 1
n = int(input())
while count <= 10**7:
    if a == 1:
        b += 1
        count += 1
        res.append(f"{a}/{b}")
        while b != 1:
            a += 1
            b -= 1
            count += 1
            res.append(f"{a}/{b}")
    elif b == 1:
        a += 1
        count += 1
        res.append(f"{a}/{b}")
        while a != 1:
            a -= 1
            b += 1
            count += 1
            res.append(f"{a}/{b}")
# print(res)
# ['1/1', '1/2', '2/1', '3/1', '2/2', '1/3', '1/4', '2/3', '3/2', '4/1']
print(res[n - 1])
"""

# 以上代码时间复杂度有点高了 果不其然超时

# 经过题解启发去除了列表，且直接在求得n所指数跳出 AC代码达成！
count = 1
a = 1
b = 1
n = int(input())
for i in range(n):
    if a == 1 and count < n:
        b += 1
        count += 1
        while b != 1 and count < n:
            a += 1
            b -= 1
            count += 1
    elif b == 1 and count < n:
        a += 1
        count += 1
        while a != 1 and count < n:
            a -= 1
            b += 1
            count += 1
print(f"{a}/{b}")
