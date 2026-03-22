# n = int(input())
# count = 0
# for i in range(2, n + 1):
#     # print(f"current: {i}")
#     for j in range(2, i + 1):
#         # print(f"current j: {j}")
#         if i % j == 0 and i != j:
#             # print("1continue")
#             break
#         elif i % j != 0:
#             # print("2continue")
#             continue
#         else:
#             count += 1
#             # print(i)
#             # print(f"count: {count}\n")
# print(count)
def judge(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


def main():
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        if judge(i):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
