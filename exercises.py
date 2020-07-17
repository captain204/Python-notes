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
    size  = len(arr)-1
    while i < size:
        if i == 0:
            if arr[i] > arr[i+1] :
                value = arr[i]
        else:
            if arr[i] > arr[i-1] and arr[i+1]:
                value = arr[i]
            max.append(value)
        i += 1
    return max


print(maxima([2,5,9,10,6,8,0]))




















