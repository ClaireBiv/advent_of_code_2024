from collections import deque

def sumTuples(x, y):
    return (x[0]+y[0], x[1]+y[1])

def enqueue(queue, set, item):
    if item not in set:
        queue.append(item)
        set.add(item)

def trailheadScore(mappa, i, j, n, m):
    trails = deque([("0",(i,j))])
    trailSet = set()

    dir = ((1,0),(0,1),(-1,0),(0,-1))

    next = 1
    while trails and next <= 9:
        if trails[0][0] != str(next):
            (i,j) = trails.popleft()[1]
            for d in dir:
                (i_n, j_n) = sumTuples((i,j),d)
                if i_n not in (-1,m) and j_n not in (-1,n):
                    if mappa[i_n][j_n] == str(next):
                        enqueue(trails, trailSet, (str(next),(i_n,j_n)))
        else:
            next += 1

    return len(trails)

file_name = "input.txt"

mappa = []
with open(file_name, 'r') as file:
    for line in file:
        mappa.append(line.strip())

n, m = len(mappa), len(mappa[0])

score = 0
for i in range(m):
    for j in range(n):
        if mappa[i][j] == "0":
            score += trailheadScore(mappa, i, j, n, m)

print(score)

