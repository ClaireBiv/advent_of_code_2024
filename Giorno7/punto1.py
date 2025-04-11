file_name = "input.txt"

def checkOperators(numbers, testValue):
    n = len(numbers)
    if n == 2:
        if numbers[0] + numbers[1] == testValue or \
            numbers[0] * numbers[1] == testValue:
            return True
        return False
    return checkOperators(numbers[:n-1], testValue/numbers[n-1]) or \
            checkOperators(numbers[:n-1], testValue-numbers[n-1])

sum = 0
with open(file_name, 'r') as file:
    for line in file:
        equation = line.split(":")
        testValue = int(equation[0])
        numbers = [int(s) for s in equation[1].split()]

        if checkOperators(numbers, testValue):
            sum += testValue

print(sum)