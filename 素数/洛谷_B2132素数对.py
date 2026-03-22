def judge(x):
    # for i in range(2, (x**1 / 2) + 1):
    #     if x % i == 0:
    #         return False
    #     return True
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


def main():
    n = int(input())
    for i in range(3, n - 1):
        if judge(i) and judge(i + 2):
            a = 1
            print(f"{i} {i+2}")
    if a == 0:
        print("empty")
    return


if __name__ == "__main__":
    main()
