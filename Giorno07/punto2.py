file_name = "input.txt"

def checkOperators(numbers, testValue):
    n = len(numbers)

    if isinstance(testValue, float) and not testValue.is_integer():
        return False
    
    testValue = int(testValue)
    if n == 2:
        if numbers[0] + numbers[1] == testValue or \
            numbers[0] * numbers[1] == testValue or \
            str(numbers[0]) + str(numbers[1]) == str(testValue):
            return True
        return False
    
    result = checkOperators(numbers[:n-1], testValue/numbers[n-1]) or \
            checkOperators(numbers[:n-1], testValue-numbers[n-1])
    
    lastNum = str(numbers[n-1])
    if str(testValue).endswith(lastNum):
        newTestValue = float(str(testValue)[:-len(lastNum)])
        return result or checkOperators(numbers[:n-1], newTestValue)
    
    return result


sum = 0
with open(file_name, 'r') as file:
    for line in file:
        equation = line.split(":")
        testValue = int(equation[0])
        numbers = [int(s) for s in equation[1].split()]

        if checkOperators(numbers, testValue):
            sum += testValue

print(sum)