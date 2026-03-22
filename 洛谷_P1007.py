# 看起来比较难 题解提供了一个绝妙的思路
# 题目没有强调对士兵个人的区分 也就是说所有士兵可以视为相同的个体
# 也就是说 当两个士兵在桥上碰面后 可以视为两人毫无碰撞地走了过去
# 所以说每个人走到终点的路程就是他离自己一开始面对的终点的距离
# 这个时候要求最小最大值 只需要对比不同朝向的时候的距离就好了

length = int(input())
n = int(input())
try:
    position = list(map(int, input().split()))
except Exception:
    pass

max, min = 0, 0
max_i, min_i = 0, 0

for i in range(n):
    r_l = length+1-position[i] # 从右端点l+1走来的距离 从左端点走来即为当前的端点
    if r_l > position[i]:
        max_i = r_l
        min_i = position[i]
    else:
        max_i = position[i]
        min_i = r_l
    if max_i > max:
        max = max_i
    if min_i > min: # 由于已知区域最小 且一定大于0 所以是>
        min = min_i
print(f'{min} {max}')