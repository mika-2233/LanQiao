def station_x(a,n,m,x):
    f = [0]*20
    f[1]=1
    for i in range(2,n):
        f[i] = f[i-1] + f[i-2] # 斐波那契数列 实际上也是一维动态规划
    # m = f[n-1-2]*a + f[n-1-1]*b + a - b
    b = (m - f[n-3]*a - a)/(f[n-2] -1)
    result = int(f[x-2]*a + f[x-1]*b +a -b)
    return result
a,n,m,x = map(int, input().split()) # 输入 5 7 32 4
the_result=station_x(a,n,m,x)
print(the_result) # 输出 13

'''
始发站上车人数 a
车站数 n
终点站下车人数 m
x站开出时车上的人数
设第二站上下车的人数为 b
上车人数=(x-3)a+(x-2)b 当x>=4 第三站上车a+b 下车b
'''