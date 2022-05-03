import time

def randomized(x, y):
    # method to generate a random number in a certain interval
    from random import randint
    return randint(x, y)


def cracker_per_digit(x):
    # method to crack a password digit per digit
    start = time.time()
    lista = list(x)
    cracked = []
    tmp = 0
    cycle = 1
    print("Cracking password per digit")
    while True:
        number = str(randomized(0, 9))
        print("Number found: ", number)
        print("Cycle: ", cycle)
        if lista[tmp] == number:
            cracked.append(number)
            tmp += 1
            print("password cracked: ", cracked)
        if tmp == len(lista):
            break
        cycle += 1

    end = time.time()
    return (end - start, cycle)


def cracker_complete_with_dict(x):
    """ method to crack a password generating and checking random numbers and 
    storing the generated numbers in a list"""
    dictionary = []
    start = time.time()
    lista = list(x)
    cracked = []
    cycle = 1
    print("Cracking password with a dictionary")
    while True:
        number = str(randomized(0, 9))
        cracked.append(number)
        if cracked == lista:
            print("Cycle: ", cycle)
            print(cracked)
            print("length dictionary: ", len(dictionary))
            break
        if len(cracked) == len(lista):
            if cracked in dictionary:
                cracked = []
            else:
                print("Cycle = ", cycle)
                print(cracked)
                dictionary.append(cracked)
                cracked = []
                cycle += 1

    end = time.time()
    return (end - start, cycle, len(dictionary))

def cracker_complete_no_dict(x):
    """ method to crack a password generating and 
    checking random numbers """
    start = time.time()
    lista = list(x)
    cracked = []
    cycle = 1
    print("Cracking password without a dictionary")
    while True:
        number = str(randomized(0, 9))
        cracked.append(number)
        if cracked == lista:
            print("Cycle: ", cycle)
            print(cracked)
            break
        if len(cracked) == len(lista):
            print("Cycle =", cycle)
            print(cracked)
            cracked = []
            cycle += 1

    end = time.time()
    return (end - start, cycle)


def cracker_incrementing(x):
    # method to crack a password incrementing numbers
    start = time.time()
    number_int = 1
    cycle = 1
    print("Cracking password incrementing digits")
    while True:
        number_str = str(number_int)
        if number_str == x:
            print("Cycle = ", cycle)
            print(number_str)
            break
        print("Cycle =", cycle)
        print(number_str)
        number_int += 1
        cycle += 1

    end = time.time()
    return (end - start, cycle)
        

while True:
    password = str(input("Type a password made of numbers: "))
    (elapsedTimeNoDict, cyclesNoDict) = cracker_complete_no_dict(password)
    (elapsedTimeWithDict, cyclesWithDict, DictSize) = cracker_complete_with_dict(password)
    (elapsedTimeIncrementing, cyclesincrementing) = cracker_incrementing(password)
    (elapsedTimePerDigit, cyclesPerDigit) = cracker_per_digit(password)
    
    print(f"Password cracked without dictionary in {elapsedTimeNoDict} seconds in {cyclesNoDict} tries")
    print(f"Password cracked with dictionary in {elapsedTimeWithDict} seconds in {cyclesWithDict} tries and with dictionary with {DictSize} elements")
    print(f"Password cracked incremeting in {elapsedTimeIncrementing} seconds in {cyclesincrementing} tries")
    print(f"Password cracked per digit in {elapsedTimePerDigit} seconds in {cyclesPerDigit} tries")
    print(f"Password cracked per digit in {elapsedTimePerDigit} seconds in {cyclesPerDigit} tries")
    print("\n")