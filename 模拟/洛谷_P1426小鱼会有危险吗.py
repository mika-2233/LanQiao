def main():
    s, x = map(float, input().split())

    v = 7
    left = s - x
    right = s + x
    fish_s = 0
    while fish_s < left:
        fish_s += v
        v *= 0.98
    if v * 0.98 <= right - fish_s:
        print("y")
        return
    else:
        print("n")
        return


if __name__ == "__main__":
    main()
