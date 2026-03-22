"""
l, r = map(int, input().split())


def judge_sp(l, r):
    primes = [True] * (r + 1)
    if r >= 0:
        primes[0] = primes[1] = False

    i = 2
    while i * i <= r:
        if primes[i]:
            primes[i * i : r + 1 : i] = [False] * len(primes[i * i : r + 1 : i])
        i += 1
    return [i for i, val in enumerate(primes) if val and i >= l]


s = judge_sp(l, r)
# print(s)
ans = len(s)
print(ans)
"""

# 此代码超出内存限制

import math
l,r=map(int,input().split())

limit=int(math.isqrt(r))+1 # 求平方根范围内的所有质数
is_prime_small = [True]*(limit+1)
is_prime_small[0]=is_prime_small[1]=False

for i in range(2,int(math.isqrt(limit))+1):
    if is_prime_small[i]:
        for j in range(i*i,limit+1,i):
            is_prime_small[j]=False

base_primes = [i for i, val in enumerate(is_prime_small) if val]
    
# 2. 初始化区间 [l, r] 的标记数组
# 长度为 r - l + 1，索引 0 对应数字 l，索引 k 对应数字 l+k
size = r - l + 1
is_prime_range = [True] * size

if l == 1:
    if size > 0: is_prime_range[0] = False # 1

# 3. 使用基础质数筛选区间 [l, r]
for p in base_primes:
    # 找到 [l, r] 范围内第一个能被 p 整除的数
    # 公式：start = max(p*p, ((l + p - 1) // p) * p)
    # 解释：
    # 1. 从 p*p 开始，因为小于 p*p 的倍数已经被更小的质数筛过了
    # 2. ((l + p - 1) // p) * p 是大于等于 l 的最小的 p 的倍数
        
    start = max(p * p, ((l + p - 1) // p) * p)
        
    # 如果起始点超过了 r，则无需处理该质数
    if start > r:
        continue
            
    # 计算 start 在 is_prime_range 数组中的索引
    # 索引 = 数值 - l
    start_index = start - l
        
    # 将区间内 p 的倍数标记为 False
    # 步长为 p
    # 使用切片赋值加速
    # 范围：从 start_index 到 size，步长 p
    is_prime_range[start_index : size : p] = [False] * len(is_prime_range[start_index : size : p])

# 4. 统计结果
ans = sum(is_prime_range)
print(ans)