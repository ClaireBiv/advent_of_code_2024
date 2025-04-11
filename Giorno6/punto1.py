from collections import deque

file_name = "input.txt"

room = []
countRow = True
i, j = 0, 0
with open(file_name, 'r') as file:
    for line in file:
        room.append(line.strip())
        if "^" in line:
            j = line.index("^")
            countRow = False
        if countRow:
            i += 1

counter = 1
dir = deque([(-1,0),(0,1),(1,0),(0,-1)])

n, m = len(room), len(room[0])

while True:
    i_next, j_next = i + dir[0][0], j + dir[0][1]
    if i_next in (-1, m) or j_next in (-1, n):
        break
    if room[i_next][j_next] in (".","X"):
        room[i] = room[i][:j] + "X" + room[i][j+1:]
        if room[i_next][j_next] == ".":
            counter += 1
        (i,j) = (i_next, j_next)
    elif room[i_next][j_next] == "#":
        dir.append(dir.popleft())

print(room)
print(counter)