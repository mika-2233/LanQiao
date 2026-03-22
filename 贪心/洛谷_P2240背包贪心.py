import sys


def main():
    input_data = sys.stdin.read().split()
    iterator = iter(input_data)

    n = int(next(iterator))
    t = int(next(iterator))

    gold_coins = []
    for _ in range(n):
        we = int(next(iterator))
        co = int(next(iterator))
        gold_coin = {"weight": we, "cost": co, "score": co / we}
        gold_coins.append(gold_coin)

    sorted_gold_coins = sorted(gold_coins, key=lambda x: -x["score"])
    del gold_coins
    # print(sorted_gold_coins)

    current = 0
    costs = 0
    # print(t)
    for i in sorted_gold_coins:
        if current + i["weight"] <= t:
            costs += i["cost"]
            current += i["weight"]
            # print(f"当前i: {i}, 背包充足全部装入，装入后收入：{costs}")
        else:
            allow = t - current
            allow_cost = (allow / i["weight"]) * i["cost"]
            costs += allow_cost
            # print(
            #     f"当前i: {i}, 背包不充足，剩余容量：{allow}\n"
            #     f"装入比例{allow / i['weight']}, 装入价值{(allow / i['weight']) * i['cost']}"
            # )
            break
    print(f"{costs:.2f}")
    return


if __name__ == "__main__":
    main()
