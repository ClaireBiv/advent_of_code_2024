file_name = "input.txt"

with open(file_name, 'r') as file:
    for line in file:
        stones = line.split()

for _ in range(25):
    newStones = []
    for i in range(len(stones)):
        if stones[i] == "0":
            newStones.append("1")
        elif len(stones[i])%2 == 0:
            mid = len(stones[i])//2
            newStones.append(stones[i][:mid])
            newStones.append(str(int(stones[i][mid:])))
        else:
            newStones.append(str(int(stones[i])*2024))
    stones = newStones
 
print(len(stones))