def judge_sp(x):
    primes = [True] * (x + 1)
    if x >= 0:
        primes[0] = False
    if x >= 1:
        primes[1] = False

    i = 2
    while i * i <= x:
        if primes[i]:
            primes[i * i : x + 1 : i] = [False] * len(primes[i * i : x + 1 : i])
        i += 1
    return [i for i, val in enumerate(primes) if val]


def main():
    n = int(input())
    primes = judge_sp(n)
    # 由于输入的是奇数 所以要减去奇数次奇数才可能为0
    # 而在所有质数中 只有2这一个偶数
    # 再由于题目要求一定要输出3个数 所以情况只有2种
    # 1.两个偶数一个奇数 2.三个奇数

    # 两个偶数一个奇数
    if n - 4 in primes:
        print(f"2 2 {n-4}")
        return
    # 三个奇数
    for i in primes[1:]:
        for j in primes[1:]:
            if n - i - j in primes:
                print(f"{i} {j} {n-i-j}")
                return


if __name__ == "__main__":
    main()
