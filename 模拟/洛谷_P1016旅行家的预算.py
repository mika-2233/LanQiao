"""
两个城市之间的距离s
汽车油箱的容量c
每升汽油能行驶的距l
出发点每升汽油的价格p
沿途油站数n
"""


def main():
    s, c, l, p, n = map(float, input().split())
    n = int(n)

    station = [(0.0, p)]
    for i in range(n):
        a, b = map(float, input().split())  # a:到这个油站的距离 b:每升汽油的价格
        station.append((a, b))
    station.append((s, 0.0))
    # print(station)
    # [(0, 2.8), (102.0, 2.9), (220.0, 2.2), (275.6, 0)]

    # 发现n最大也就6 所以我们可以遍历所有结果找到最优
    # 1.在当前油站需要加的油，就是能够支持到达下一个单价更低的加油站的量
    # 2.如果在当前油站加满也无法到达下一个比它油价更低的油站，就加满油箱，尽量到达
    # 3.如果在这个油站即使加满也不能到达下一个油站或者终点，说明无解

    max_run = c * l  # 满油最大行驶距离
    n_total = len(station)
    for i in range(1, n_total):
        if station[i][0] - station[i - 1][0] > max_run:
            # 条件三符合
            print("No Solution")
            return

    k = 0.0  # 油箱中到达下一个加油站时剩余油量可以继续走的路程
    ans = 0.0
    curr_idx = 0

    while curr_idx < n_total - 1:
        current_station = station[curr_idx]
        target_idx = -1
        cheaper_idx = -1

        for i in range(curr_idx + 1, n_total):
            dist_diff = station[i][0] - current_station[0]

            if dist_diff > max_run:
                break  # 前往这个油站超出了最大续航

            # 寻找比当前油价更便宜的站点
            if station[i][1] < current_station[1]:
                cheaper_idx = i
                break

            if target_idx == -1 or station[i][1] < station[target_idx][1]:
                # 如果没有更便宜的，记录当前的
                target_idx = i

        next_idx = -1
        if cheaper_idx != -1:
            # 找到了更便宜的油站：让车刚好跑到该油站
            next_idx = cheaper_idx
            need_dist = station[next_idx][0] - current_station[0]

            if k < need_dist:  # 如果现有的油不足，就补足差额
                buy_dist = need_dist - k
                ans += (buy_dist / l) * current_station[1]
                k = need_dist

            # 到达下一站，减去消耗的油
            k -= station[next_idx][0] - current_station[0]

        elif target_idx != -1:
            # 没有找到更便宜的，策略2
            next_idx = target_idx
            need_dist = station[next_idx][0] - current_station[0]

            if k < max_run:
                fill_dist = max_run - k
                ans += (fill_dist / l) * current_station[1]
                k = max_run
            k -= need_dist

        curr_idx = next_idx

    print(f"{ans:.2f}")


if __name__ == "__main__":
    main()
