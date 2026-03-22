import sys


def main():
    input_data = sys.stdin.read().split()
    iterator = iter(input_data)

    n = int(next(iterator))
    d = []
    for _ in range(n):
        d.append(int(next(iterator)))

    del input_data
    del iterator

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if d[j] < d[i]:
                ans += 1

    print(ans)
    return


"""
逆序对的定义在序列 a[1..n] 中，
若存在下标 i 和 j（1 ≤ i < j ≤ n）满足 a[i] > a[j]，
则称 (a[i], a[j]) 构成一个逆序对。

旋转可以一次多反转序列，实际上每一个逆序对都需要一次操作，
所以我们求逆序对数量即可。
"""


if __name__ == "__main__":
    main()
