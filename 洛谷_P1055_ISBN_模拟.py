origin = input()
origin_list = []
for char in origin:
    origin_list.append(char)
without_dash = origin.replace('-', '')

reco_total=0
for i in range(len(without_dash)-1):
    reco_total += int(without_dash[i])*(i+1)
reco = reco_total % 11
if str(reco)==origin[-1]:
    print('Right')
elif reco==10:
    if origin[-1]=='X':
        print('Right')
    else:
        origin_list[-1] = 'X'
        print(''.join(origin_list))
else:
    origin_list[-1] = str(reco)
    print(''.join(origin_list))