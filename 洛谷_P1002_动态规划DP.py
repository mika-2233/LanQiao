x,y,hx,hy=map(int,input().split())

b=[]
a=[(2,1),(1,2),(-1,2),(-2,1),
   (-2,-1),(-1,-2),(1,-2),(2,-1)]
for dx,dy in a:
    nx,ny=hx+dx,hy+dy
    if 0<=nx<=x and 0<=ny<=y:
        b.append((nx,ny))
b.append((hx,hy))

dp=[[0]*(y+1) for _ in range(x+1)]

if (0,0) not in b:
    dp[0][0]=1
for i in range(x+1):
    for j in range(y+1):
        if i==0 and j==0:
            continue
        if (i,j) in b:
            dp[i][j]=0
        else:
            left=dp[i-1][j] if i>0 else 0
            down=dp[i][j-1] if j>0 else 0
            dp[i][j]=left+down
print(dp[x][y])
