import sys
from array import array


def main():
    input_data = sys.stdin.read().split()
    iterator = iter(input_data)

    n = int(next(iterator))

    d = array("i", [0]) * 1000001
    for _ in range(n):
        a = int(next(iterator))
        b = int(next(iterator))
        d[a] += 1
        if b + 1 < 1000001:
            d[b + 1] -= 1
    # print(d)
    local = 0
    maxx = -114
    for i in d:
        local += i
        if local > maxx:
            maxx = local
    print(maxx)
    return


if __name__ == "__main__":
    main()
