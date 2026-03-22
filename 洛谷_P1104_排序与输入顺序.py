n = int(input())

name = []
year = []
month = []
day = []
idx_order = []  # 记录输入顺序

for i in range(n):
    line = input().split()
    name.append(line[0])
    year.append(int(line[1]))
    month.append(int(line[2]))
    day.append(int(line[3]))
    idx_order.append(i)  # 第 i 个输入

for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        # 比较 j 和 j+1
        y1, m1, d1, in1 = year[j], month[j], day[j], idx_order[j]
        y2, m2, d2, in2 = year[j+1], month[j+1], day[j+1], idx_order[j+1]

        need_swap = False

        if y1 > y2:
            need_swap = True
        elif y1 == y2 and m1 > m2:
            need_swap = True
        elif y1 == y2 and m1 == m2 and d1 > d2:
            need_swap = True
        elif y1 == y2 and m1 == m2 and d1 == d2:
            # 同生日：后输入的（in2 > in1）应该排在前面
            # 当前 j 是 in1，j+1 是 in2
            # 如果 in1 < in2（即 j 先输入，j+1 后输入），那么 j+1 应该在 j 前面
            if in1 < in2:
                need_swap = True
        if need_swap:
            # 交换所有字段
            name[j], name[j+1] = name[j+1], name[j]
            year[j], year[j+1] = year[j+1], year[j]
            month[j], month[j+1] = month[j+1], month[j]
            day[j], day[j+1] = day[j+1], day[j]
            idx_order[j], idx_order[j+1] = idx_order[j+1], idx_order[j]
            swapped = True
    if not swapped:
        break

for nm in name:
    print(nm)