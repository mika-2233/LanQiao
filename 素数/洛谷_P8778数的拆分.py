def odd_even(n):
    lis = [0, 0, 0, 0]
    if n % 2 == 0:  # 如果是偶数
        count2 = 0
        a = n
        while True:
            if a == 1:
                # print(count)
                return lis  # 没有第二个因数 直接返回False
            elif a % 2 == 0:  # 如果余数是偶数 继续除
                count2 += 1
                lis[0] = count2
                a = a // 2
            else:  # 如果余数是奇数 调到下面的循环除以3或5
                break
        current = a
        count3 = count5 = count7 = 0
        while True:
            if current == 1:
                # print(count)
                return lis
            elif current % 3 == 0:
                count3 += 1
                lis[1] = count3
                current = current // 3
            elif current % 5 == 0:
                count5 += 1
                lis[2] = count5
                current = current // 5
            elif current % 7 == 0:
                count7 += 1
                lis[3] = count7
                current = current // 7
            else:
                return False  # 其中一个因数是质数 无法满足题目要求 返回False
    else:  # 如果是奇数
        return False


def main():
    t = int(input())
    result = []
    for _ in range(t):
        n = int(input())
        if n == 1 or n == 2:
            # print("输入为1或2")
            result.append("no")
            continue
        lr = odd_even(n)
        if not lr:
            # print("判定为no")
            result.append("no")
        elif (
            lr[0]
            and lr[1]
            and lr[2]
            or lr[0]
            and lr[1]
            and lr[3]
            or lr[1]
            and lr[2]
            and lr[3]
            or lr[0]
            and lr[1]
            and lr[2]
            and lr[3]
        ):  # 有三个或者四个因数
            # print("有两个以上因数")
            result.append("no")
        elif lr[0] > 1 and not lr[1] and not lr[2] and not lr[3]:  # 是2的幂
            # print("是2的幂")
            result.append("yes")
        elif lr[0] > 1 and lr[1] > 1 and not lr[2] and not lr[3]:  # 因数2和3的幂大于1
            # print("因数2和3")
            result.append("yes")
        elif lr[1] > 1 and lr[2] > 1 and not lr[0] and not lr[3]:  # 因数3和5的幂大于1
            # print("因数3和5")
            result.append("yes")
        elif lr[2] > 1 and lr[3] > 1 and not lr[0] and not lr[1]:  # 因数5和7的幂大于1
            # print("因数5和7")
            result.append("yes")
        else:
            # print("其余情况因数幂数不够")
            result.append("no")
    for i in result:
        print(i)
    return


# if __name__ == "__main__":
#     main()
# 以上方法错误 奇数也是可以存在满足的拆分的
