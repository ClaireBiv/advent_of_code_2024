file_name = "input1.txt"


l1, l2 = [], []

with open(file_name, 'r') as file:
    for line in file:
        num = line.split()
        l1.append(int(num[0]))
        l2.append(int(num[1]))

oracolo = {}
for num in l2:
    if num in oracolo:
        oracolo[num] += 1
    else:
        oracolo[num] = 1

sum = 0
for num in l1:
    if num in oracolo:
        sum += num * oracolo[num]

print(sum)