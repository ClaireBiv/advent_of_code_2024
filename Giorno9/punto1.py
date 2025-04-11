file_name = "input.txt"

blockLayout = []
empty = False
id = 0
with open(file_name, 'r') as file:
    for line in file:
        for c in line.strip():
            if empty:
                for _ in range(0, int(c)):
                    blockLayout.append(".")
            else:
                for _ in range(0, int(c)):  
                    blockLayout.append(str(id))
                id += 1
            empty = not empty

n = len(blockLayout)
i, j = 0, n-1

while True:
    while blockLayout[i] != ".":
        i += 1

    while blockLayout[j] == ".":
        j -= 1

    if i < j:
        blockLayout[i] = blockLayout[j]
        blockLayout[j] = "."
    else:
        break

sum, x = 0, 0
while blockLayout[x] != ".":
    sum += x * int(blockLayout[x])
    x += 1

print(sum)