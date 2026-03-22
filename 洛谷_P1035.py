k = int(input())
s = 0
ss = 1
while True:
    s += 1 / ss
    if s > k:
        print(ss)
        break
    ss += 1