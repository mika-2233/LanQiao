a = input()
c = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4]
ans = 0
for i in a:
    if i >= "a" and i <= "z":
        ans += c[ord(i) - ord("a")]
    elif i == " ":
        ans += 1
print(ans)
