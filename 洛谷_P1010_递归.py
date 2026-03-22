def int_to_2power(n,i=0):
    if n>2**i:
        return int_to_2power(n,i+1)
    elif n<2**i:
        n=n-(2**(i-1))
        return [i-1] + int_to_2power(n,0)
    elif n==2**i:
        return [i]
    elif n==1:
        return [0]
    elif n==0:
        return []

def print_power(powers_list):
    parts = []
    for p in powers_list:
        if p == 0:
            parts.append("2(0)")
        elif p == 1:
            parts.append("2")
        elif p == 2:
            parts.append("2(2)")
        else:
            sub_powers = int_to_2power(p)
            sub_string = print_power(sub_powers)
            parts.append(f"2({sub_string})")
    return "+".join(parts)

# 符合洛谷的提交格式 使用input然后直接print output
n = int(input())
powers_list = int_to_2power(n)
output = print_power(powers_list)
print(output)