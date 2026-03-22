n=int(input())
# 这样的数据量我们直接打表 先计算出表
# def check(x):
#     sum_val = 0
#     # 从 1 枚举到 x 的平方根 (i*i <= x)
#     i = 1
#     while i * i <= x:
#         if x % i == 0:
#             sum_val += i
#             # 如果 i 不是平方根，则加上对应的另一个因数 x/i
#             if i * i != x:
#                 sum_val += x // i  # 使用整除 // 确保结果是整数
#         i += 1
    
#     # 判断真因子之和是否等于 x
#     # 原代码逻辑：sum - x == x  =>  sum == 2 * x
#     return sum_val - x == x

# def main():
#     # 遍历 2 到 10000
#     for i in range(2, 10001):
#         if check(i):
#             print(i)

# if __name__ == "__main__":
#     main()

if n >=6:
    print(6)
if n>=28:
    print(28)
if n>=496:
    print(496)
if n>=8128:
    print(8128)
