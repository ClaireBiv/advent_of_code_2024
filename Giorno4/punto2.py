file_name = "input.txt"

def trovaXmas(griglia, i, j, n, m):
    if i in (0, m-1) or j in (0, n-1):
        return 0
    if (griglia[i+1][j+1],griglia[i-1][j-1]) in (("M","S"),("S","M")) and \
        (griglia[i-1][j+1],griglia[i+1][j-1]) in (("M","S"),("S","M")):
            return 1
    return 0

griglia = []
with open(file_name, 'r') as file:
    for line in file:
        griglia.append(line.strip())
print(griglia)

n = len(griglia)
m = len(griglia[0])

counter = 0

for i in range(m):
    for j in range(n):
        if griglia[i][j] == "A":
            counter += trovaXmas(griglia, i, j, n, m)

print(counter)
