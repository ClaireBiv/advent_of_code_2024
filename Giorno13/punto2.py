import re
import math

file_name = "test2.txt"

def subLists(x, y):
    return [x[0]-y[0], x[1]-y[1]]

def multListInt(x, l):
    return [x*l[0], x*l[1]]

def divLists(a,b):
    return int(min(a[0]/b[0], a[1]/b[1]))

def maxComDiv(a,b):
    return min(math.gcd(a[0],b[0]), math.gcd(a[1],b[1]))

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

    mcd = maxComDiv(A,B)

    counter = divLists(prize, B)
    print(counter)

    for j in range(counter,-1,-1):
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