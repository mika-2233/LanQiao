import sys
from array import array


def fix():
    input_data = sys.stdin.read().split()
    iterator = iter(input_data)

    n = int(next(iterator))
    p = int(next(iterator))

    first_val = int(next(iterator))

    # 使用array创建差分数组d 类型为i 有符号整数
    d = array("i", [0]) * n
    prev = first_val
    for i in range(1, n):
        curr = int(next(iterator))
        d[i] = curr - prev
        prev = curr

    for _ in range(p):
        x = int(next(iterator))
        y = int(next(iterator))
        z = int(next(iterator))
        d[x - 1] += z
        if y < n:
            d[y] -= z

    del input_data
    del iterator

    current_val = first_val + d[0]
    minn = current_val
    for i in range(1, n):
        current_val += d[i]
        if current_val < minn:
            minn = current_val
    print(minn)
    return


# 即使是只用了一个array也超内存吗 洛谷 你这家伙……
if __name__ == "__main__":
    fix()


def main():
    n, p = map(int, input().split())
    score = list(input().split())  # ['1', '1', '1']
    # print(score)
    d = [0] * n
    for i in range(1, n):
        d[i] = int(score[i]) - int(score[i - 1])
    for i in range(p):
        x, y, z = map(int, input().split())
        d[x - 1] += z
        try:
            d[y] -= z
            # print(f"当前d: {d}")
        except IndexError:
            # print(f"当前d: {d}")
            continue

    current_val = int(score[0]) + d[0]
    minn = current_val
    for i in range(1, n):
        current_val += d[i]
        if current_val < minn:
            minn = current_val
    # print(score)
    print(minn)
    return


# 代码超内存且一个测试点错误
# if __name__ == "__main__":
#     main()
