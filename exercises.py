"""Sample python programming exercises"""

"""Find the average of all elements in a list"""

def average(arr):
   return sum(arr) // len(arr)




"""Find the sum of elements of a two dimensional list"""
def sumDimensional(arrOne,arrTwo):
    return sum (arrOne) + sum(arrTwo)




"""Find the largest element in a list"""
def largest(arr):
    i = 0
    for value in arr:
       if value > arr[i]:
           arr[i] = value
    return arr[i]


"""Find the smallest element in a list"""

def smallest(arr):
    i = 0
    for value in arr:
        if value < arr[i]:
            arr[i] = value
    return  arr[i]


"""Find the second largest number in the list"""

def secondLargest(arr):
    i = 0
    for value in arr:
        temp = arr[i]
        if value > arr[i]:
            arr[i] = value
    return temp

#print(secondLargest([2,5,8,9,10,110]))


"""Print all maxima in a list A value is a maximum 
    if the value before and after its index are smaller 
    than it is or does not exist"""

def maxima(arr):
    max = []
    i = 0
    while i < len(arr)-1:
        if arr[i+1] > arr[i] and arr[i+1] > arr[i+2]:
            value=arr[i+1]
        max.append(value)
        return max
    i += 1

print(maxima([2,5,1,7,4,1]))



"""Print all alternate elements of a python list"""
def alternate(arr):
    return(arr[1::2])





"""Given a list with value 0 or 1 write a program to segregate 0 on the left side and 1 on the right side"""
def segregate(arr):
    right = []
    left = []
    for value in arr:
        if value < 1:
            left.append(value)
        else:
            right.append(value)
    return left + right


"""Given a list of intervals merge all overlapping intervals
   input:{[1,4],[3,6],[8,10]}
   output:{[1,6],[8,10]}
"""



"""Reversing a list in place"""
def reverse(arr):
    start = 0
    end = len(arr)-1
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -=1
    return arr
#print(reverse([2,5,1,7,4,1]))





"""Segregate zeros ones and twos"""

def segregate_twos(arr):
    zero = []
    ones = []
    twos = []
    for value in arr:
        if value < 1:
            zero.append(value)
        elif value < 2:
            ones.append(value)
        else:
            twos.append(value)
    return zero + ones + twos


"""Check if a list contains duplicate elements"""
def duplicate_check(arr):
    if len(arr) == len(set(arr)):
        return "Duplicates exist"
    else:
        return "List contain no duplicates "


"""Find the duplicate elements in a list of size n where each element is in the range 0 to n-1"""
def duplicate(arr):
    size = len(arr)
    repeated = []
    for i in range(size):
        k = i + 1
        for j in range(k,size):
            if arr[i] == arr[j] and arr[i] not in repeated:
                repeated.append(arr[i])
    return repeated

print(duplicate([2,5,1,7,4,1,2,4,7]))



