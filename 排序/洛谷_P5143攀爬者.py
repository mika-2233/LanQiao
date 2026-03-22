import sys
import numpy as np


def distance(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


def main():
    input_data = sys.stdin.read().split()
    iterator = iter(input_data)

    n = int(next(iterator))
    d = []
    for _ in range(n):
        x = int(next(iterator))
        y = int(next(iterator))
        z = int(next(iterator))
        d.append((x, y, z))

    sorted_d = sorted(d, key=lambda x: (x[2]))
    # print(sorted_d) # [(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5)]
    del d

    ans = float()
    for i in range(n - 1):
        ans += distance(sorted_d[i + 1], sorted_d[i])
    print(f"{ans:.3f}")
    return


if __name__ == "__main__":
    main()
