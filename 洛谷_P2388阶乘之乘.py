def sum_floor(n, m):
    q = n // m
    return q * (n + 1) - m * q * (q + 1) // 2


n = int(input())
ans = 0
power = 5
while power <= n:
    ans += sum_floor(n, power)
    power *= 5
print(ans)

# 上面这个是公式 可以大大减少时间复杂度 实际上这个题目的规律我们已经发现了
# 每当n可以被5整除，阶乘的结果就会多一个0，如4！=24,5！=120,
# 且当n是5的幂时，是多少幂就会多多少个0，例如25!比24！多了两个0
# 常规做法是遍历每一个数 这样的时间复杂度为O(n)实在是有点多 所以我也懒得写了
