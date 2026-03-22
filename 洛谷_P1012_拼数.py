# def num(length,list):
#     for i in range(length-1):
#         local = list[i]
#         next = list[i+1]
#         if local*(10**(len(next)))+next<next*(10**(len(local)))+local:
#             list[i],list[i+1] = list[i+1],list[i]
#             num(length,list)
#     result_str = ''.join(map(str, list))
#     result_int = int(result_str)
#     return result_int

# length = int(input())
# list = list(map(str, input().split()))
# result = num(length,list)
# print(result)

# 字符串到整数的多次转换大大降低速度 并加大了内存消耗 直接在字符串对比会高效许多
def num(length, list):
    swapped = False
    for i in range(length-1):
        a, b = list[i], list[i+1]
        if a+b < b+a:
            list[i], list[i+1] = list[i+1], list[i]
            swapped = True
    if swapped:
        num(length, list)
    return list

length = int(input())
list = list(map(str,input().split()))
sorted_list = num(length, list)
result_str = ''.join(sorted_list)
result_int = int(result_str)
print(result_int)