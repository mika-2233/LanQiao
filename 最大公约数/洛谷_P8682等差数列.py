import math


def main():
    """
    设公差为d，那么对于任意 i，j，有 gcd(a_i,a_j)=k*d。
    因为等差数列中任意两项的差都必然是多个d累加的结果
    但直接列举时间复杂度是O(n^2)

    我们需要想起任意两项的差都是公差的倍数 题目要求我们求出最短的等差数列
    所以这个公差需要最大
    于是我们就需要计算所有排序后相邻数的差的最大公因数
    """
    n = int(input())
    inp = list(map(int, input().split()))
    inp.sort()

    if n == 1:
        print(1)
        return

    ans = inp[1] - inp[0]

    # 计算所有相邻数的差的最大公因数 具体操作为依次与第一个相邻差求最大公因数
    for i in range(2, n):
        diff = inp[i] - inp[i - 1]
        ans = math.gcd(ans, diff)

    if ans == 0:  # 求得差值为0，意味着数组中所有数字都是一样的
        print(n)
        return
    else:
        # 计算提供的数列中差值最大的两项
        lar = inp[-1] - inp[0]
        print(lar // ans + 1)
        return


if __name__ == "__main__":
    main()
