file_name = "input.txt"

def dfs(field, i, j, symb, n, m):
        visited = set((i,j))
        stack = [(i,j)]

        area, peri = 0, 0
        while stack:
            x, y = stack.pop()

            if (x,y) in visited:
                continue

            if x in (-1,m) or y in (-1,n) or field[x][y] != symb:
                peri += 1
                continue

            visited.add((x,y))
            field[x][y] = "."

            area += 1 
            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))

        return (area, peri)

field = []
with open(file_name, 'r') as file:
    for line in file:
        field.append(list(line.strip()))

n, m = len(field), len(field[0])

sum = 0
for i in range(m):
    for j in range(n):
        if field[i][j] != ".":
            a, p = dfs(field, i, j, field[i][j], n, m)
            sum += a*p
            
print(sum)