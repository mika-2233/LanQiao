"""
第一个月末:w0(1+r)-w
第二个月末:(w0(1+r)-w)(1+r)-w
所以这个方程只有r这一个未知数，但是r(利率)既出现在底数中，也出现在分母中
而且还有m次幂，所以无法直接解方程
但是这个函数具有单调性：r越高，需要换的钱就越多
所以我们可以使用二分查找来逼近真实值
题目已经给出了范围0-3.0
具体步骤：
取中间值作为猜测利率，代入方程看钱多了还是少了
如果多了说明猜测的利率过高，将右边界缩小到mid
如果少了，将左边界缩小到mid
重复这两个过程直到范围达到精度0.1%也就是0.001
"""


def main():
    line = input().split()
    w0 = float(line[0])
    w = float(line[1])
    m = int(line[2])
    # w0贷款本金
    # w每次还款金额
    # m还款月数

    def check(rate):
        current_debt = w0
        for _ in range(m):
            current_debt = current_debt * (1 + rate) - w
        return current_debt

    left = 0.0
    right = 3.0

    while right - left > 0.0001:  # 精度作为结束条件，高一到两个数量级
        mid = (left + right) / 2.0
        remaining = check(mid)

        if remaining > 0:  # 最后剩余的欠款大于0，说明才的利率高了
            right = mid
        else:  # 剩余欠款小于等于0，说明利率猜低了或者刚刚好
            left = mid

    print(f"{left * 100:.1f}")
    return


if __name__ == "__main__":
    main()
