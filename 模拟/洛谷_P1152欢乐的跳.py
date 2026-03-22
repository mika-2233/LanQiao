import sys


def main():
    input_data = sys.stdin.read().split()
    iterator = iter(input_data)

    n = int(next(iterator))
    a = []
    for i in range(n):
        a.append(int(next(iterator)))
    b = [0] * 114514
    for i in range(1, n):
        b[abs(a[i - 1] - a[i])] = True
    # print(b)
    for i in range(1, n):
        if not b[i]:
            print("Not jolly")
            return
    print("Jolly")
    return


if __name__ == "__main__":
    main()
