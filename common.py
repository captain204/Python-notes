"""
List of common functions

"""



"""Write a method that will return all elements of the integer list given list and its size"""
def SumArray(arr):
    size = len(arr)
    total = 0
    index = 0
    while index < size:
        total += arr[index]
        index += 1
    return total


"""Sequential search"""

def SequentialSearch(arr, value):
    size = len(arr)
    i = 0
    while i < size:
        if value == arr[i]:
            return True
        i += 1
    return False

""" Binary search """
def BinarySearch(arr, value):
    size = len(arr)
    low = 0
    high = size - 1
    while low <= high:
        mid = low + (high - low) // 2
        #print(low)
        #print(high)
        if arr[mid] == value:
            return True
        else:
            if arr[mid] < value:
                low = mid + 1
            else:
                high = mid-1
    return False

#print(BinarySearch([2,4,6,8,10,12,14],14))

"""Function to reverse a list"""

def reverseArray(arr):
    i = 0
    j = len(arr) - 1

    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1
    return arr



#print(reverseArray([2,4,6,8,10,12,14]))


"""Function to reverse a list in place with a start and end value"""
def reverseList(arr,start,end):
    i = start
    j = end

    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1

    return arr

#print(reverseList([2,4,6,8,10,12,14],0,6))


"""Function to rotate a list in place"""
def rotateList(arr,k):
    n = len(arr)
    reverseList(arr,0,k-1)

    reverseList(arr,k,n-1)
    return reverseList(arr, 0, n - 1)



#print(rotateList([2,4,6,8,10,12,14],2))

"""Recursive function that returns the factorial of a number"""

def factorial(i):
    if i <=1:
        return 1
    return i * factorial(i-1)


print(factorial(5))