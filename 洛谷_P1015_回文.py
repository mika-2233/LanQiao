# def palindrome(base, m):
#     steps = 0
#     if not base==10:
#         num_Base10 = int(m,base)
#     else:
#         num_Base10 = int(m)
#     while steps<=30:
#         str_Base10 = str(num_Base10)
#         str_reverse = str_Base10[-1::-1]
#         if str_Base10 == str_reverse:
#             print(f'STEP={steps}')
#             return steps
#         num_Base10 += int(str_reverse)
#         steps+=1
#     print('Impossible!')

# n = int(input().strip())
# m = input().replace(' ', '')
# result = palindrome(n,m)

# 理论上来说上面的算法逻辑是没有问题的 但是涉及输入的换行符问题

# 涉及了高精度计算的内容
n = int(input().strip())
m = input().strip().replace(' ', '')
a = []
for char in m:
    try:
        a.append(int(char,base=n))
    except Exception:
        pass
a = a[::-1] # 低位在前以便进位

steps = 0
while steps<=30:
    reverse = a[::-1]
    if a==reverse:
        break
    
    # 由于题目要求
    new_a = []
    carry = 0
    for i in range(len(a)):
        total = a[i] + reverse[i] + carry
        new_a.append(total % n)
        carry = total // n
    if carry:
        new_a.append(carry)
    a = new_a
    steps+=1
if steps<=30:
    print(f'STEP={steps}')
else:
    print("Impossible!")