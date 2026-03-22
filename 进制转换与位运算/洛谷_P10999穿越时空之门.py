ans = 0
for i in range(1, 2025):
    # 转换为2进制
    # result = []
    a = i
    ii2 = 0
    while True:
        if not a:
            break
        b = a % 2
        # result.append(str(b))
        ii2 += b
        a //= 2
    # print(result)

    # 转换为4进制
    # result4 = []
    a4 = i
    ii4 = 0
    while True:
        if not a4:
            break
        b4 = a4 % 4
        # result4.append(str(b4))
        ii4 += b4
        a4 //= 4
    # print(result4)

    # 对比两个进制下各位数之和
    if ii2 == ii4:
        ans += 1
print(ans)
