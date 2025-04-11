import re

file_name = "input.txt"

def subLists(x, y):
    return [x[0]-y[0], x[1]-y[1]]

def multListInt(x, l):
    return [x*l[0], x*l[1]]

def isMultiplo(a,b):
    r = 0
    while all(i>0 for i in a):
        r += 1
        a = subLists(a,b)
        if a == [0,0]:
            return True, r
    return False, None

def count(numbers):
    A, B, prize = numbers

    for j in range(100,-1,-1):
        r = subLists(prize,multListInt(j,B))
        if r[0] < 0 or r[1] < 0:
            continue
        isM, i = isMultiplo(r,A)
        if isM:
            return i, j
    return None


sum = 0
num = []
with open(file_name, 'r') as file:
    for line in file:
        if line == "\n":
            num = []
            continue

        coord = [int(x) for x in re.findall(r'\d+', line)]
        num.append(coord)

        if "Prize" in line:
            c = count(num)
            if c != None:
                sum += c[0]*3 + c[1]

print(sum)