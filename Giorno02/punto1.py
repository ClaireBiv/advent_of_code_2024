file_name = "input2.txt"


def isSafe(report):
    n = len(report)

    if all(report[i]-report[i+1] in (1,2,3) \
           for i in range(n-1)) or \
        all(report[i]-report[i+1] in (-1,-2,-3) \
            for i in range(n-1)):
        return True
    else:
        return False
    

safe_reports = 0
with open(file_name, 'r') as file:
    for line in file:
        report = [int(s) for s in line.split()]
        if isSafe(report):
            safe_reports += 1

print(safe_reports)