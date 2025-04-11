file_name = "input.txt"

def trovaParola(griglia, word, i, j, n, m, direzione):
    for l in range(len(word)):
        if i in (-1, m) or j in (-1, n):
            return 0
        if word[l] == griglia[i][j]:
            i,j = i + direzione[0], j + direzione[1]
        else:
            return 0
    return 1

griglia = []
with open(file_name, 'r') as file:
    for line in file:
        griglia.append(line.strip())

word = "XMAS"

n = len(griglia)
m = len(griglia[0])

directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
              (1, 1), (1, -1), (-1, 1), (-1, -1)]

counter = 0

for i in range(m):
    for j in range(n):
        if griglia[i][j] == word[0]:
            for d in directions:
                counter += trovaParola(griglia, word, i, j, n, m, d)

print(counter)
