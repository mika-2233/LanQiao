import sys


def main():
    input_data = sys.stdin.read().split()
    iterator = iter(input_data)

    n = int(next(iterator))
    students = []
    for k in range(n):
        ch = int(next(iterator))
        ma = int(next(iterator))
        en = int(next(iterator))
        total = ch + ma + en
        student = {"id": k + 1, "chinese": ch, "total": total}
        students.append(student)

    # 排序规则：降序总分，如果相同，降序语文，如果相同，升序学号
    sorted_students = sorted(
        students, key=lambda x: (-x["total"], -x["chinese"], x["id"])
    )

    for i in sorted_students[:5]:
        print(f"{i['id']} {i['total']}")


if __name__ == "__main__":
    main()
