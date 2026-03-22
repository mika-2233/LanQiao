h, s1, v, l, k, n = map(float, input().split())
s2 = s1

position = []
for i in range(int(n)):
    position.append(float(i))

t = float(((h-k)/5)**0.5)
t1 = float((h/5)**0.5)
tt = float(1.0/v)

s1 -= v*t
s2 -= v*t1

count = 0
for x in position:
    if (s2-0.0001)<=x<=(s1+l+0.0001):
        count += 1
print(count)