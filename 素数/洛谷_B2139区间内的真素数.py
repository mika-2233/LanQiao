def judge(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


def main():
    a = []
    m, n = map(int, input().split())
    for i in range(m, n + 1):
        if judge(i):
            re = int(str(i)[::-1])
            if judge(re):
                # print(f"添加：{i}")
                a.append(i)
    if not a:
        print("No")
    else:
        print(",".join(map(str, a)))


if __name__ == "__main__":
    main()
