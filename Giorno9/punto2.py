file_name = "input.txt"

fileBlocks, emptyBlocks = [], []
empty = False
id = 0
with open(file_name, 'r') as file:
    for line in file:
        n = 0
        for c in line.strip():
            digit = int(c)
            if empty:
                if digit != 0:
                    emptyBlocks.append([digit, (n, n+digit-1)])
                    n += digit
            else:
                fileBlocks.append([digit, (n, n+digit-1), id])
                n += digit
                id += 1
            empty = not empty

sum = 0
for block in reversed(fileBlocks):
    for em in emptyBlocks:
        blockLen, emptyLen = block[0], em[0]
        blockInt, emptyInt = block[1], em[1]
        if blockLen <= emptyLen and blockInt > emptyInt:
            block[1] = (emptyInt[0], emptyInt[0]+blockLen-1)
            em[0] -= blockLen
            if em[0] == 0:
                emptyBlocks.remove(em)
            else:
                em[1] = (emptyInt[0]+blockLen, emptyInt[1])
            break
    
    for i in range(block[1][0],block[1][1]+1):
        sum += i*block[2]

print(sum)