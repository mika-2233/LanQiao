import sys
from array import array


def main():
    input_data = sys.stdin.read().split()
    iterator = iter(input_data)

    up = 6  # 向上一层6秒
    down = 4  # 向下一层4秒
    opent = 5  # 开门5秒
    leave = 1  # 下一个人1秒

    # 电梯从0层开始 返回0层任务结束
    n = int(next(iterator))
    b = array("i", [0]) * n
    for i in range(n):
        b[i] = int(next(iterator))
    del input_data
    del iterator

    sorted_b = sorted(b, key=lambda x: x)
    del b
    # print(sorted_b) [2, 2, 3, 4]
    dest = 0
    anst = 0
    for i in sorted_b:
        if i == dest:
            anst += leave
            # print(f"当前i: {i}, 当前anst: {anst}")
            continue
        anst += (i - dest) * up + opent + leave
        dest = i
        # print(f"当前i: {i}, 当前anst: {anst}")
    # print(f"上到顶层: {dest}")
    anst += dest * down
    print(anst)
    return


if __name__ == "__main__":
    main()
