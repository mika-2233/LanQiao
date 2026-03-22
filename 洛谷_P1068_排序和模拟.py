import math
n,m=map(int,input().split())

t=math.floor(m*1.5)
list=[]
for i in range(n):
    l,r=map(int,input().split())
    list.append([l,r])

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # 分解：将列表分成两半
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # 递归排序左半部分
    right_half = merge_sort(arr[mid:])  # 递归排序右半部分
    # 合并：将两个有序子列表合并
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    # 比较两个子列表的元素，按顺序合并
    while i < len(left) and j < len(right):
        if left[i][1] > right[j][1]:
            sorted_arr.append(left[i])
            i += 1
        elif left[i][1] < right[j][1]:
            sorted_arr.append(right[j])
            j += 1
        else:
            if left[i][0] < right[j][0]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
    # 将剩余的元素添加到结果中
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

sort=merge_sort(list)

line=sort[t-1][1] # 录取分数线
count=0
last=[]
for i in range(n):
    if sort[i][1]>=line:
        count+=1
        last.append(sort[i])

print(f'{last[-1][1]} {count}')
for k in last:
    print(f'{k[0]} {k[1]}')