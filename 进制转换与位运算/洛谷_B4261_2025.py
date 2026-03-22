x = int(input())
for i in range(1, 2026):
    if (x & i) + (x | i) == 2025:
        print(i)
        break
"""
上面的方法为暴力枚举法
下面还有优雅的推断
根据这四种情况 我们可以推断出 (a and b)+(a or b)=a+b
情况 1：a 是 0，b 也是 0，此时 aandb=0，aorb=0，a+b=0；
情况 2：a 是 0，b 是 1，此时 aandb=0，aorb=1，即 (aandb)+(aorb)=1，而 a+b=1，两者相等；
情况 3：a 是 1，b 是 0，此时与情况 2 完全一致；
情况 4：a 是 1，b 也是 1，此时 aandb=1，aorb=1，即 (aandb)+(aorb)=2，而 a+b=2，两者相等；
"""
# x = int(input())
# i = 2025 - x
# print(i)
