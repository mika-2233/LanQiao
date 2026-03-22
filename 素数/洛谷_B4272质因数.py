temp_primes = {}


def judge(x):
    if x == 1 or x == 0:
        return False
    elif x in temp_primes:
        return True
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    temp_primes[x] = True
    return True


temp_odd_even = {}


def odd_even(n):
    if n in temp_odd_even:
        return temp_odd_even[n]
    if n % 2 == 0:  # 如果是偶数
        count = 0
        a = n
        while True:
            if a == 1:
                # print(count)
                temp_odd_even[n] = count
                return count
            elif a % 2 == 0:  # 如果余数是偶数 继续除
                count += 1
                a = a // 2
            else:  # 如果余数是奇数 调到下面的循环除以3或5
                break
        current = a
        while True:
            if current == 1:
                # print(count)
                temp_odd_even[n] = count
                return count
            elif current % 3 == 0:
                count += 1
                current = current // 3
            elif current % 5 == 0:
                count += 1
                current = current // 5
            elif current % 7 == 0:
                count += 1
                current = current // 7
            else:
                temp_odd_even[n] = count + 1
                return count + 1  # 是质数
    else:  # 如果是奇数
        if judge(n):  # 先判定是不是一个质数 如果是直接返回1
            return 1
        # 不是质数 除以3,5,7
        count = 0
        current = n
        while True:
            if current == 1:
                # print(count)
                temp_odd_even[n] = count
                return count
            elif current % 3 == 0:
                count += 1
                current = current // 3
                print(f"除以3，结果为：{current}")
            elif current % 5 == 0:
                count += 1
                current = current // 5
                print(f"除以5，结果为：{current}")
            elif current % 7 == 0:
                count += 1
                current = current // 7
                print(f"除以7，结果为：{current}")
            else:  # 商是质数
                temp_odd_even[n] = count + 1
                return count + 1


def main():
    n, m = map(int, input().split())
    # 对于n==m的处理
    if n == m == 1:
        print(0)
        return
    elif n == m == 2:
        print(1)
        return
    elif n == m:  # 如果n和m相等且不在1,2这两个数中
        print(odd_even(n))
        return

    # 对于范围的处理
    # 在范围内2的幂是质因数最多的 所以找出范围内是否有2的幂
    # print("范围判断")
    i = 1
    have = False
    while True:
        a = 2**i
        # print(f"当前幂：{i}")
        if a > m and have:  # 范围中有2的幂 打印最大的那个
            print(i - 1)
            return
        elif a == m:
            print(i)
            return
        elif a > m and not have:  # 如果超出了范围且没有找到 跳出循环
            # print("没有2的幂")
            break
        elif a < n:
            i += 1
        elif n <= a < m:
            i += 1
            have = True

    # 如果没有找到
    maxx = 0
    if n % 2 == 0:
        for i in range(n, m + 1, 2):
            # print(f"当前数：{i}；最大质因数：{maxx}")
            if maxx < odd_even(i):
                maxx = odd_even(i)
    else:
        for i in range(n + 1, m + 1, 2):
            if maxx < odd_even(i):
                maxx = odd_even(i)
    print(maxx)
    return


# 以上方法超时
if __name__ == "__main__":
    main()


def solve():
    n, m = map(int, input().split())
    if m < 2:
        print(0)
        return

    dp = [0] * (m + 1)  # dp[i]=数字i的质因数总个数
    for i in range(2, m + 1):
        if dp[i] == 0:  # 如果i是质数
            # 对于i的每一个倍数j（在这里i是j的最小质因数）
            for j in range(i, m + 1, i):
                # 这个倍数j将会比上一个倍数多一个质因数
                # 2-1 4-2 8-3 16-4
                # 13-1 26//13=2 39//13=3
                # 3-1 6-2 9//3=3 12//3=4
                dp[j] = dp[j // i] + 1
    print(max(dp[n : m + 1]))


# 狗屎啊这个超时更严重
# if __name__ == "__main__":
#     solve()
