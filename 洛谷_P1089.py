def main():
    n = 0
    save = 0
    for i in range(12):
        spend = int(input())
        n+=300-spend
        if n<0:
            print(f'-{i+1}')
            return
        while n>=100:
            save+=100
            n-=100
    last = int(save*1.2+n)
    print(last)

if __name__ == "__main__":
    main()