import re

file_name = "input.txt"

sum = 0
enabled = True
with open(file_name, 'r') as file:
    for line in file:
        pattern1 = "mul\(\d{1,3},\d{1,3}\)"
        pattern2 = "don't\(\)"
        pattern3 = "do\(\)"
        instructions = re.findall(f"{pattern1}|{pattern2}|{pattern3}", line)
        for e in instructions:
            if e == "do()":
                enabled = True
            elif e == "don't()":
                enabled = False
            else:
                if enabled:
                    fatt = [int(n) for n in re.findall(r'\d+', e)]
                    sum += fatt[0] * fatt[1]
        
print(sum)