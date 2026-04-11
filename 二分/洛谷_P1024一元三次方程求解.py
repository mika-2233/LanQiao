def main():
    line = input().split()
    a = float(line[0])
    b = float(line[1])
    c = float(line[2])
    d = float(line[3])

    def fc(x):
        return a * (x**3) + b * (x**2) + c * x + d

    # 我们可以枚举-100到100之间的所有长度为1的区间
    # 因为解之间的距离大于等于1，所以一个区间内只有一个解
    # 这符合了二分的规则
    ans = []
    s = 0
    for i in range(-100, 100):
        left = i
        right = i + 1
        x1 = fc(left)
        x2 = fc(right)

        if not x1:
            ans.append(f"{left:.2f}")
            s += 1
        if x1 * x2 < 0:
            while right - left >= 0.001:  # 二分精度大于精度要求一个数量级
                mid = (left + right) / 2
                if fc(mid) * fc(right) <= 0:
                    left = mid
                else:
                    right = mid
            ans.append(f"{right:.2f}")
            s += 1
        if s == 3:
            break  # 找到三个解早停
    print(" ".join(ans))
    return


if __name__ == "__main__":
    main()
