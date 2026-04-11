"""
从1到n这些数中，含有2、0、1、9的数字的和是多少
样例输入40
样例输出574

也就是说我们需要判断每一个位上的数字
之前我们的思路是转换为字符串单个比较
但是这样的时间复杂度必然过高
我们在这个题目的官方题解中得到了思路
"""

n = int(input())

ans = 0
for i in range(1, n + 1):  # 遍历范围内的所有数
    local = i
    flag = False

    while local > 0:
        jud = local % 10  # 判断当前数的最后一位，也就是个位
        if jud == 2 or jud == 0 or jud == 1 or jud == 9:
            flag = True
        local = local // 10  # 将当前数的个位去除

    if flag:  # 如果这个数满足要求，加到ans中
        ans += i

print(ans)
