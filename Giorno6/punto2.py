from collections import deque

file_name = "input.txt"

def checkObstacle(i, j, dir):
    ban = [(i,j,dir[0])]
    dir.append(dir.popleft())
    #print("chiamata")
    while True:
        #print((i,j,dir[0]))
        i_next, j_next = i + dir[0][0], j + dir[0][1]
        if i_next in (-1, m) or j_next in (-1, n):
            return False
        if room[i_next][j_next] in ("#","O"):
            if (i,j,dir[0]) in ban:
                return True
            ban.append((i,j,dir[0]))
            #print(ban)
            dir.append(dir.popleft())
        else:
            (i,j) = (i_next, j_next)
        

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

counter = 0
dir = deque([(-1,0),(0,1),(1,0),(0,-1)])

n, m = len(room), len(room[0])
b=0
while True:
    #print(i,j)
    i_next, j_next = i + dir[0][0], j + dir[0][1]
    if i_next in (-1, m) or j_next in (-1, n):
        break
    if room[i_next][j_next] == "#":
        dir.append(dir.popleft())
    else:
        room[i_next] = room[i_next][:j_next] + "O" + room[i_next][j_next+1:]
        dir_alt = deque(dir)
        if checkObstacle(i,j,dir_alt):
            counter += 1
        room[i_next] = room[i_next][:j_next] + "." + room[i_next][j_next+1:]
        (i,j) = (i_next, j_next)
    b +=1
print(counter)