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
    n = int(input())
    k = 4
    while k <= n:
        for j in range(2, k + 1):
            if judge(j):
                if judge(k - j):
                    print(f"{k}={j}+{k-j}")
                    break
        k += 2

    return


if __name__ == "__main__":
    main()
