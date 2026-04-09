n = int(input())
a = []
for i in range(n):
    hight, left, right = map(int, input().split())
    a.append((hight, left, right, i + 1))
a_sor = sorted(a, key=lambda x: x[0])
# print(a)
# print(a_sor)
"""
[(2, 0, 2, 1), (4, 1, 3, 2), (3, 1, 3, 3), (5, 3, 4, 4), (1, 1, 5, 5)]
[(1, 1, 5, 5), (2, 0, 2, 1), (3, 1, 3, 3), (4, 1, 3, 2), (5, 3, 4, 4)]
"""
ran = {}
# 初始化最低层
if n > 0:
    firstH, firstL, firstR, _ = a_sor[0]
    ran[firstH] = (0, firstL, firstR, 0)

    for k in a_sor[1:]:
        currH, l, r, ind = k
        bottomL_h = 0  # 记录左侧支撑的高度
        bottomR_h = 0  # 记录右侧支撑的高度

        # 遍历所有比当前层低的层（已排序，所以是前面的所有层）
        # 注意：这里不需要 reversed，因为我们要找的是“最高”的那个支撑
        # 但为了逻辑清晰，我们遍历所有比它低的，看谁能接住它
        for j in a_sor:
            if j[0] >= currH:
                break  # 只考虑比当前低的

            j_h, j_l, j_r, _ = j

            # 检查左侧边缘 l 是否落在方块 j 的范围内 [j_l, j_r]
            if j_l <= l <= j_r:
                # 如果方块 j 比当前记录的 bottomL_h 更高，更新它
                if j_h > bottomL_h:
                    bottomL_h = j_h

            # 检查右侧边缘 r 是否落在方块 j 的范围内 [j_l, j_r]
            if j_l <= r <= j_r:
                # 如果方块 j 比当前记录的 bottomR_h 更高，更新它
                if j_h > bottomR_h:
                    bottomR_h = j_h

        ran[currH] = (bottomL_h, l, r, bottomR_h)

# print(ran)
"""
{1: (0, 1, 5, 0), 2: (0, 0, 2, 1),
 3: (2, 1, 3, 1), 4: (2, 1, 3, 1), 
 5: (1, 3, 4, 1)}
"""

res = []
for k in a:
    currH = k[0]  # 当前高度
    info = ran.get(currH)
    if info:
        idxLh = info[0]
        idxRh = info[3]
        resL = 0
        resR = 0

        if idxLh != 0:
            for item in a_sor:
                if item[0] == idxLh:
                    resL = item[3]
                    break
        if idxRh != 0:
            # 找到高度为 idxR_h 的方块编号
            for item in a_sor:
                if item[0] == idxRh:
                    resR = item[3]
                    break

    res.append(f"{resL} {resR}")

print("\n".join(res))
