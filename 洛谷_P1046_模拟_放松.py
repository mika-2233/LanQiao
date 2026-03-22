def simulation(list,hight):
    hight += 30
    count = 0
    for i in list:
        if i<=hight:
            count+=1
    return count

list = list(map(int,input().split()))
hight = int(input())
result = simulation(list,hight)
print(result)