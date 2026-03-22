k,n = map(int,input().split())

def ten_t_two(num):
    if num == 0:
        return "0"
    result = ""
    while num > 0:
        result = str(num % 2) + result
        num //= 2
    return result

def any_t_ten(num_s,base):
    result = 0
    p = 0
    for i in reversed(num_s):
        result += int(i)*(base**p)
        p+=1
    return result

m=ten_t_two(n)
mm=any_t_ten(m,k)
print(mm)