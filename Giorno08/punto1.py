file_name = "input.txt"

def distTuples(x, y):
    return (x[0]-y[0], x[1]-y[1])

def sumTuples(x, y):
    return (x[0]+y[0], x[1]+y[1])

def placeAntinodes(griglia, char, n, m):
    counter = 0
    for x in range(len(char)):
        for y in range(x+1,len(char)):
            dist = distTuples(char[x],char[y])
            (i1,j1) = sumTuples(char[x],dist)
            (i2,j2) = distTuples(char[y],dist)

            if (-1 < i1 < m) and (-1 < j1 < n) and griglia[i1][j1] != "#":
                griglia[i1] = griglia[i1][:j1] + "#" + griglia[i1][j1+1:]
                counter += 1

            if (-1 < i2 < m) and (-1 < j2 < n) and griglia[i2][j2] != "#":
                griglia[i2] = griglia[i2][:j2] + "#" + griglia[i2][j2+1:]
                counter += 1
    return counter

griglia = []
with open(file_name, 'r') as file:
    for line in file:
        griglia.append(line.strip())

n = len(griglia)
m = len(griglia[0])

frequencies = {}
for i in range(m):
    for j in range(n):
        char = griglia[i][j]
        if char != ".":
            if char not in frequencies:
                frequencies[char] = [(i,j)]
            else:
                frequencies[char].append((i,j))

counter = 0
for c in frequencies:
    counter += placeAntinodes(griglia, frequencies[c], n, m)

print(counter)