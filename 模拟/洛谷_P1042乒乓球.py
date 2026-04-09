import sys

input_data = sys.stdin.read()
clean_data = input_data.replace("\n", "")
inp = list(clean_data)
# print(result)

hua_count11 = 0
counter_count11 = 0

hua_count21 = 0
counter_count21 = 0

result11 = []
result21 = []
for i in inp:
    iavi11 = abs(hua_count11 - counter_count11)
    if (hua_count11 >= 11 or counter_count11 >= 11) and iavi11 >= 2:
        result11.append(f"{hua_count11}:{counter_count11}")
        hua_count11 = counter_count11 = 0

    iavi21 = abs(hua_count21 - counter_count21)
    if (hua_count21 >= 21 or counter_count21 >= 21) and iavi21 >= 2:
        result21.append(f"{hua_count21}:{counter_count21}")
        hua_count21 = counter_count21 = 0

    if i == "W":
        hua_count11 += 1
        hua_count21 += 1
    elif i == "L":
        counter_count11 += 1
        counter_count21 += 1
    else:
        result11.append(f"{hua_count11}:{counter_count11}")
        result21.append(f"{hua_count21}:{counter_count21}")
        break
# print(result11)
# print(result21)

print("\n".join(result11))
print()
print("\n".join(result21))
