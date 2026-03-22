def main():
    gov_expect = int(input())
    cost_list = []
    sales_list = []
    while True:
        cost, sales = map(int, input().split())
        if cost == -1 and sales == -1:
            break
        cost_list.append(cost)
        sales_list.append(sales)
    count = len(cost_list)
    decrease = int(input())

if __name__ == "__main__":
    main()