def main():
    n, base = map(int, input().split())

    res = []

    a = n
    if base > -10:
        while True:
            if not a:
                break
            b = floor(a / base)
            res.append(str(b))
            a //= base
        print(f"{n}={''.join(res[::-1])}(base{base})")
        return
    else:
        e = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        while True:
            if not a:
                break
            b = a % base
            print(f"b={b}")
            if b >= 10:
                res.append(e[b - 10])
                a //= base
            else:
                res.append(str(b))
                a //= base
        print(f"{n}={''.join(res[::-1])}(base{base})")


if __name__ == "__main__":
    main()
