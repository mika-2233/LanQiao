s=int(input())

def f(x):
    if x == 1:
        return 0
    ans = 1  # 1 是所有 x > 1 的真约数
    i = 2
    while i * i <= x:
        if x % i == 0:
            ans += i
            if i != x // i:  # 避免平方根重复加
                ans += x // i
        i += 1
    return ans

i = s
while True:
    t = f(i)
    if f(t) == i and i != t:
        print(i, t)
        break
    i += 1