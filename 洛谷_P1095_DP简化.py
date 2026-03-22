m,s,t=map(int,input().split())

flash=0
run=0
for i in range(1,t+1):
    if m>=10: # 蓝够了就闪 并同时模拟跑步
        m-=10
        flash+=60
        run+=17
    else: # 蓝不够 在最优的基础上跑
        if flash>run:
            run=flash
        run+=17
        m+=4 # 这一边模拟在原地回蓝
    
    if max(flash,run)>=s:
        print('Yes')
        print(i)
        break
else:
    print('No')
    print(max(flash,run))