def main():
    a = list(input().strip())
    b = list(input().strip())

    flag = 1
    # 如果不等长就跳出
    if len(a) != len(b):
        flag = 0

    arr = [0] * 26
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == a[j] and b[i] != b[j] or a[i] != a[j] and b[i] == b[j]:
                flag = 0
            # 将当前的字母计入统计表中统计存在性
            if "A" <= a[i] <= "Z":
                arr[ord(a[i]) - ord("A")] = 1
            else:
                flag = 0
    # print(arr)
    # 如果少了字母就跳出
    if 0 in arr:
        flag = 0

    inp = list(input().strip())
    # print(inp)
    res = []
    for x in inp:
        if x in a and ord("A") <= ord(x) <= ord("Z"):
            idx = a.index(x)
            res.append(b[idx])
        else:
            flag = 0
    if not flag:
        print("Failed")
        return
    print("".join(res))
    return


if __name__ == "__main__":
    main()
