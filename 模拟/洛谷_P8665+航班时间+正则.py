import sys
import re


def format() -> int:
    line = sys.stdin.readline()

    # (\d+):(\d+):(\d+)  -> 匹配开始时间 h1:m1:s1
    # \s+                -> 空格
    # (\d+):(\d+):(\d+)  -> 捕获结束时间 h2, m2, s2
    # (?:\s+\(+(\d+)\))? -> 非捕获组，可选部分：匹配空格 + "(+" + 数字 + ")"
    pattern = r"(\d+):(\d+):(\d+)\s+(\d+):(\d+):(\d+)(?:\s+\(\+(\d+)\))?"

    match = re.match(pattern, line.strip())
    h1, m1, s1 = int(match.group(1)), int(match.group(2)), int(match.group(3))
    h2, m2, s2 = int(match.group(4)), int(match.group(5)), int(match.group(6))
    d = int(match.group(7)) if match.group(7) else 0

    start_sec = h1 * 3600 + m1 * 60 + s1
    end_sec = h2 * 3600 + m2 * 60 + s2

    return (d * 86400 + end_sec) - start_sec


def main():
    """
    去程=飞行时间+时差
    回程=飞行时间-时差
    所以去程+回程再/2就是飞行时间
    """
    n = int(sys.stdin.readline().strip())

    ans = []
    for _ in range(n):
        time1 = abs(format())
        time2 = abs(format())
        # print(f"time1: {time1}; time2: {time2}")

        one_way_time = (time1 + time2) // 2

        h = one_way_time // 3600
        m = (one_way_time % 3600) // 60
        s = one_way_time % 60

        ans.append([h, m, s])

    for i in ans:
        print(f"{i[0]:02d}:{i[1]:02d}:{i[2]:02d}")
    return


if __name__ == "__main__":
    main()
