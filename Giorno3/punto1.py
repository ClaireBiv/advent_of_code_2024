import re

file_name = "input.txt"

sum = 0
with open(file_name, 'r') as file:
    for line in file:
        pattern = "mul\(\d{1,3},\d{1,3}\)"
        instructions = re.findall(pattern, line)
        for e in instructions:
            fatt = [int(n) for n in re.findall(r'\d+', e)]
            sum += fatt[0] * fatt[1]

print(sum)