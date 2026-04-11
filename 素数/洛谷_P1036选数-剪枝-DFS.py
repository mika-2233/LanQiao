def isprime(x):
    if x == 1:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


def main():

    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))

    ans = 0

    def dfs(now, current_sum, start_idx):
        """
        now: 当前已经选了多少个数
        current_sum: 当前选中的数的总和
        start_idx: 本次循环开始遍历的数组下标
        """

        nonlocal ans

        if now == k:
            if isprime(current_sum):
                ans += 1
            return

        # 剪枝
        remain = k - now

        """
        数组一共有n个元素
        为了满足后面有足够的数可以选，我们不需要遍历到n
        所以当前枚举的索引极限是n-remain+1
        例如：n=5, k=3。如果我们已经选了1个(now=1)，还需要2个(remain=2)。
        我们最远只能枚举到第 5-2+1 = 4 个数。如果选了第5个数，后面就不够凑齐3个数了。
        """
        limit = n - remain + 1

        for i in range(start_idx, limit + 1):
            dfs(now + 1, current_sum + a[i], i + 1)

    dfs(0, 0, 1)
    print(ans)
    return


if __name__ == "__main__":
    main()
