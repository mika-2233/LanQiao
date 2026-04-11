"""
在数学中，两个数对的 最大公因数*最小公倍数=数对的乘积
"""


def main():
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    x0, y0 = map(int, input().split())

    ans = 0
    for i in range(x0, y0 + 1):  # 数对中的数不可能小于最大公因数，不可能大于最小公倍数
        if (
            x0 * y0 % i == 0  # 如果当前数i可以整除乘积，说明是乘积的因数
            and gcd(i, x0 * y0 / i) == x0
        ):  # 且这个数组的最大公约数等于期待值
            # 理论上来说，似乎只需要检查下面那个gcd就可以了，还需要上面另外的检查的原因是
            # 保证当前数所得到的最小公倍数是整数--基于数学的严谨性
            # 减少计算量，如果每一个都计算GCD，时间复杂度过高
            ans += 1

    print(ans)
    return


if __name__ == "__main__":
    main()
