def main(l,r):
    ans=0
    for i in range(l,r+1):
        x=i
        while x>0:
            if x%10==2:
                ans+=1
            x=x//10
    print(ans)
    return

if __name__=='__main__':
    l,r=map(int,input().split())
    main(l,r)


