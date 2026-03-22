import sys


def main():
    input_data = sys.stdin.read().split()
    iterator = iter(input_data)

    n = int(next(iterator))
    d = []
    for i in range(1, n + 1):
        person = {"time": int(next(iterator)), "index": i}
        d.append(person)
    sorted_d = sorted(d, key=lambda x: (x["time"], x["index"]))
    del d
    # print(sorted_d)

    times = [0] * n
    total = 0
    result = []
    for k in range(n):
        result.append(str(sorted_d[k]["index"]))
        if not k:  # 第一个人不需要等待
            continue
        # 最后一个人的打水时间忽略
        # 每个人的等待时间等于前一个的人的等待时间加上前一个人的打水时间
        times[k] = times[k - 1] + sorted_d[k - 1]["time"]
        total += times[k]
    average_time = total / n
    print(" ".join(result))
    print(f"{average_time:.2f}")
    return


if __name__ == "__main__":
    main()
