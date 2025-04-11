file_name = "input.txt"

def distTuples(x, y):
    return (x[0]-y[0], x[1]-y[1])

def sumTuples(x, y):
    return (x[0]+y[0], x[1]+y[1])

def placeAntinodes(griglia, char, n, m):
    
    if len(char) == 1:
        return 0

    counter = 0
    for x in range(len(char)):
        for y in range(x+1,len(char)):
            dist = distTuples(char[x],char[y])

            (i1,j1) = sumTuples(char[x],dist)
            while (-1 < i1 < m) and (-1 < j1 < n):
                if griglia[i1][j1] != "#":
                    griglia[i1] = griglia[i1][:j1] + "#" + griglia[i1][j1+1:]
                    counter += 1
                (i1,j1) = sumTuples((i1,j1),dist)
            
            (i2,j2) = distTuples(char[y],dist)
            while (-1 < i2 < m) and (-1 < j2 < n):
                if griglia[i2][j2] != "#":
                    griglia[i2] = griglia[i2][:j2] + "#" + griglia[i2][j2+1:]
                    counter += 1
                (i2,j2) = distTuples((i2,j2),dist)

    return counter

griglia = []
with open(file_name, 'r') as file:
    for line in file:
        griglia.append(line.strip())

n = len(griglia)
m = len(griglia[0])

counter = 0
frequencies = {}
for i in range(m):
    for j in range(n):
        char = griglia[i][j]
        if char != ".":
            if char not in frequencies:
                frequencies[char] = [(i,j)]
            else:
                frequencies[char].append((i,j))
            griglia[i] = griglia[i][:j] + "#" + griglia[i][j+1:]
            counter += 1


for c in frequencies:
    counter += placeAntinodes(griglia, frequencies[c], n, m)

print(counter)