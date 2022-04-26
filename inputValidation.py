def validateInput(systemArgs):
    if not validNumArgs(systemArgs) or (len(systemArgs) > 1 and not validateArrayLength(systemArgs[1])):
        return False
    return True

def validNumArgs(systemArgs):
    if len(systemArgs) > 2:
        print("This program only accepts 2 arguments\n'python simulation.py <optional: number>'")
        return False
    return True

def validateArrayLength(arrayLength):
    try:
        lengthOfArray = int(arrayLength)
    except ValueError:
        print("Your second argument must be a number greater than 1\n'python simulation.py <optional: number>'")
        return False

    if lengthOfArray <= 1:
        print("Your second input must be a number bigger than 1\n'python simulation.py <optional: number>'")
        return False

    return True