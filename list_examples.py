from random import randrange

def listExample():
    arr = [0] * 10
    i = 0
    while i < 10:
        arr[i] = i
        i += 1
    return arr


#print(listExample())

"""Function that prints random number"""

def randomNum(num):
    arr = [0] * num
    i = 0
    while i < num:
        randomValue = randrange(9)
        arr[i] = randomValue
        i += 1
    return arr

print(randomNum(12))
print(randomNum(11))
print(randomNum(50))

"""Function that returns the sum of a list"""

def sum(list):
    total = 0

    for value in list:
        total += value
    return total


print(sum([2,4]))