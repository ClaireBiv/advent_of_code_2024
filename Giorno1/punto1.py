file_name = "test.txt"


l1, l2 = [], []

with open(file_name, 'r') as file:
    for line in file:
        num = line.split()
        print(num[1])
        l1.append(int(num[0]))
        l2.append(int(num[1]))

l1.sort()
l2.sort()

sum = 0
for i in range(len(l1)):
    diff = abs(l1[i] - l2[i])
    sum += diff

print(sum)