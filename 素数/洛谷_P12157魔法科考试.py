# 质数就是素数
"""
def judge(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


n, m = map(int, input().split())
ln = list(map(int, input().split()))
lm = list(map(int, input().split()))
count = 0
l = []
for i in ln:
    for j in lm:
        a = i + j
        if a <= n + m:
            if judge(a) and a not in l:
                l.append(a)
                count += 1
                # print(f"组合：{i}+{j}")
print(count)
"""


# 此法超时
def judge_sp(x):
    """
    埃拉托斯特尼筛法
    输入所要判断质数的范围上界
    返回一个包含所有数字对应索引的布尔值列表
    """
    is_prime = [True] * (x + 1)  # 先假设所有数都是质数
    # 0和1都不是质数 直接修改
    if x >= 0:
        is_prime[0] = False
    if x >= 1:
        is_prime[1] = False

    i = 2
    while i * i <= x:
        # 如果i是质数
        if is_prime[i]:
            # 将i的倍数标注为合数（False)
            # 原c++ for (int j=i*i; j<=x; j+=i)
            # 这里使用Python的切片赋值更方便
            # 从i*i开始，每隔i个位置的元素，范围上界为x+1
            is_prime[i * i : x + 1 : i] = [False] * len(is_prime[i * i : x + 1 : i])
        i += 1
    # return is_prime
    # 更改：直接输出包含所有质数的列表
    return [i for i, val in enumerate(is_prime) if val]


def main():
    n, m = map(int, input().split())
    ln = set(map(int, input().split()))
    lm = set(map(int, input().split()))
    max_x = n + m
    is_prime = judge_sp(max_x)
    if len(ln) > len(lm):
        ln, lm = lm, ln  # 总是遍历更短的集合
    count = 0
    for p in is_prime:
        found = False
        for a in ln:
            b = p - a
            if b in lm:
                found = True
                break
        if found:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
