def main():
    # FIXME:重构了代码
    n, r = map(int, input().split())

    original_n = n
    digits = []

    char_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if n == 0:
        print(f"0=0(base{r})")
        return

    while n != 0:
        # 计算余数
        reminder = n % r
        # 计算商
        quotient = n // r
        """
        但是结果里不能有小于0的因数，所以当余数小于0的时候我们还需要转换
        原理：我们只需要将商+1，余数-除数即可，
        因为余数（绝对值）一定小于除数，所以这样就可以将余数装换为正数
        证明：（商+1）*除数+（余数-除数）=商*除数+除数+余数-除数=商*除数+余数=被除数
        不管对于什么语言，
        被除数=商*除数+余数
        所以上面这个公式对于所有语言都是成立的
        故Python中虽然取余的方法不同 也不需要特别修改      
        """
        if reminder < 0:
            reminder -= r
            quotient += 1
        # 将余数转换为对应的字符并存入列表
        digits.append(char_map[reminder])
        # 更新n为新的商，继续下一轮循环
        n = quotient

    digits.reverse()  # 由于我们是倒序获取余数的，所以需要反转列表

    result_str = "".join(digits)
    print(f"{original_n}={result_str}(base{r})")
    return


if __name__ == "__main__":
    main()
