h = list(map(int, input().split()))
count = len(h)
dp = [1] * count # dp[i]=以第i个数为结尾的最长不增子序列的长度

# O(n^2)动态规划方法
result = 0
for i in range(1, count):
    dp[i] = 1 # 自己占用一个长度
    for j in range(0, i):
        if h[j]>=h[i]:
            dp[i] = max(dp[i], dp[j]+1)
    result = max(result, dp[i]) # 遍历所有以num[i]结尾的最长不增子序列长度 求最长的 这里利用了已有的遍历
print(result)

# O(nlogn)方法 用数组构建一个栈
l = []
for height in h:
    if not l or height<=l[-1]: # 如果栈是空的或者炮弹高度低于最后一个 那么直接入栈
        l.append(height)
    else: # 否则二分法查找一个刚好小于height的位置索引 并进行替换
        left, right = 0, len(l)-1
        target = -1
        while left<=right:
            mid = (left+right)//2
            if l[mid]<height:
                target = mid
                right = mid-1
            else:
                left = mid+1
        l[target] = height
print(len(l))

s = []
for height in h:
    if not s or height>s[-1]: # 如果没有拦截系统发射过或者已有的拦截系统无法拦截 那就发射一个导弹
        s.append(height)
    else: # 否则二分法找到一个刚好大于等于h[i]的位置索引 并进行替换 表示拦截导弹 并计入当前可到达最大高度
        left,right = 0, len(s)-1
        target = -1
        while left<=right:
            mid = (left+right)//2
            if s[mid]>=height:
                target = mid
                right = mid -1
            else:
                left = mid+1
        s[target] = height
print(len(s))