k = int(input())
have = False
for s in range(10000, 30001):
    s1 = s // 100
    s2 = (s % 10000) // 10
    s3 = s % 1000
    if s1 % k == 0 and s2 % k == 0 and s3 % k == 0:
        print(s)
        have = True
if not have:
    print("No")
