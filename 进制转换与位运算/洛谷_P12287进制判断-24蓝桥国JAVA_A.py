"""
输入样例
2
1010 23
A1 160

输出样例
10
-1
"""


def main():
    n = int(input())
    inp_data = [input().split() for _ in range(n)]
    # [['1010', '23'], ['A1', '160']]
    result = [0] * n
    for i in range(n):
        count = 0
        x = inp_data[i][0]
        x_max = int(inp_data[i][1])
        for base in [2, 4, 8, 16]:
            try:
                val = int(x, base)
                if val <= x_max:
                    result[i] = val
                    count += 1
            except ValueError:
                # 如果无法转换 那么尝试下一个进制
                continue
        # print(f"当前输入的count: {count}")
        if count > 1 or count == 0:
            result[i] = -1

    for k in result:
        print(k)


if __name__ == "__main__":
    main()
