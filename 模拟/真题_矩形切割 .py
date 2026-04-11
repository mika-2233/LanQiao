# a = 5
# b = 3
# 正确结果为4
a = 2019
b = 324
# 正确结果为21

ans = 0
while a + b != 0:
    print(f"当前a:{a},b:{b}")
    if a < b:
        b = b - a
        ans += 1
    elif b < a:
        a = a - b
        ans += 1
    else:
        ans += 1
        break

print(ans)
