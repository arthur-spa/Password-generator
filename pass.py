import random
import string

looping = True
length = None
numbers = None
upperCase = None
numberOfPass = None


def YorN(var):
    if (var == "y"):
        print("yes \n")
        return True
    else:
        print("no \n")
        return False


def isNum(var):
    try:
        newVar = int(var)
        return newVar
    except:
        print(var, "is not a number ! \n")
        return False


def passGenerator(lgth, num, UC, numPass):
    for i in range(numPass):
        choice = None
        if (num):
            if(UC):
                choice = string.ascii_uppercase + string.digits + string.ascii_lowercase
            else:
                choice = string.ascii_lowercase + string.digits
        else:
            if(UC):
                choice = string.ascii_uppercase + string.ascii_lowercase
            else:
                choice = string.ascii_lowercase

        print(''.join((random.choice(choice) for i in range(lgth))))


print("Welcome on Pass generator !")

while looping:
    lenghtAnyType = input("How long ? (number of characters) ")
    if (isNum(lenghtAnyType)):
        length = isNum(lenghtAnyType)
        print(length, "\n")
        looping = False

looping = True
isNumbers = input("Do you want numbers ? (y/n) ")
numbers = YorN(isNumbers)
isUpperCase = input("Mix of upperCase and lowerCase characters ? (y/n) ")
upperCase = YorN(isUpperCase)

while looping:
    numberOfPassAnyType = input("How many passes do you want ? (number) ")
    if (isNum(numberOfPassAnyType)):
        numberOfPass = isNum(numberOfPassAnyType)
        print(numberOfPass, "\n")
        looping = False

passGenerator(length, numbers, upperCase, numberOfPass)
