import sys
from array import array


def main():
    input_data = sys.stdin.read().split()
    iterator = iter(input_data)

    n = int(next(iterator))
    m = int(next(iterator))

    # 构建差分数组
    dif = array("i", [0]) * (n + 1)
    l_arr = array("i", [0]) * m
    r_arr = array("i", [0]) * m
    for _ in range(m):
        l = int(next(iterator))
        r = int(next(iterator))
        l_arr[_] = l
        r_arr[_] = r
        dif[l - 1] += 1
        if r < n:
            dif[r] -= 1

    # 输入结束清缓存
    del input_data
    del iterator

    cnt0 = 0  # 全局0，即所有操作都没有涉及到的地方的计数
    cnt1_prefix = array("i", [0]) * (
        n + 1
    )  # 从商品库存中值为1的个数 向左拓展一个0以便计算
    current_val = 0
    for i in range(1, n + 1):
        # 得到当前索引的前缀和 实际上也是真实货量 由于起始都是0 所以直接用差分数组就可以
        current_val += dif[i - 1]
        # print(f"current_val: {current_val}")
        cnt1_prefix[i] = cnt1_prefix[i - 1]  # 先继承上一个位置的值
        if (
            current_val == 0
        ):  # 如果当前索引的前缀和是0 说明当前商品的库存就是0，全局0加1
            cnt0 += 1
        elif current_val == 1:  # 如果当前索引的前缀和是1，将这个标记为1
            # 当范围内的操作不被接受的时候 这个地方将变为0 需要所以需要标记
            # 实际表示为1-i里1的总数
            cnt1_prefix[i] += 1
    # print(dif)  # [1, 1, 0, 0, -1, 0]
    # print(cnt1_prefix)  # [0, 1, 1, 1, 1, 2]

    # 回应每个操作不进行的情况
    res = []
    for i in range(m):
        l = l_arr[i]
        r = r_arr[i]
        count_ones_in_range = cnt1_prefix[r] - cnt1_prefix[l - 1]
        ans = cnt0 + count_ones_in_range
        res.append(str(ans))

    print("\n".join(res))
    return


if __name__ == "__main__":
    main()
