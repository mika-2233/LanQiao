import sys
from array import array


def main():
    input_data = sys.stdin.read().split()
    iterator = iter(input_data)

    n = int(next(iterator))

    d = array("i", [0]) * (n + 1)
    for i in range(n):
        d[i] = int(next(iterator))

    del input_data
    del iterator

    ans = d[0]  # 第一个坑是需要坑深度的操作消除的
    for k in range(1, n):
        if d[k] > d[k - 1]:
            # 如果这个坑是一个更深的坑 那就先填这个坑
            # 这样小坑就会顺带一起被填 于是这个小坑就在和大坑的操作中一起被填了
            # 一个大坑要填多少次 取决于前一个小坑的深度
            # 因为我们的判断是从第一个坑开始的
            # 当这个大坑前的小坑被处理完后 就无法再与第一个坑一起处理了
            # 所以小坑的大小实际上就是这个大坑可以与之前的坑一起处理的次数
            # 故一个大坑的操作次数为
            ans += d[k] - d[k - 1]
    print(ans)
    return


if __name__ == "__main__":
    main()
