from collections import defaultdict

file_name = "input.txt"

with open(file_name, 'r') as file:
    for line in file:
        stones: dict[str,int] = {k: 1 for k in line.split()}

for _ in range(75):
    newStones = defaultdict(int)
    for stone, num in stones.items():
        if stone == "0":
            newStones["1"] += num
        elif len(stone)%2 == 0:
            mid = len(stone)//2
            newStones[stone[:mid]] += num
            newStones[str(int(stone[mid:]))] += num
        else:
            newStones[str(int(stone)*2024)] += num
    stones = newStones

print(sum(stones.values()))