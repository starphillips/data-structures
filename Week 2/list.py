
# 1. Write a Python program to sum all the items in a list.

def mySum(list):
    if list == []:
        return 'The list is empty'
    sum = 0
    for v in list:
        sum = sum + v
    return sum


# 2. Write a Python program to multiplies all the items in a list.

def myMult(l):
    if not l:
        return "The list is empty"
    mult = 1
    for v in myList:
        mult = mult * v
    return mult

# 3. Write a Python program to get the largest number from a list.


def myLarge(l):
    if len(l) == 0:
        return 'The list is empty'
    largest = l[0]
    for v in myList:
        if largest < v:
            largest = v
    return largest

# 4. Write a Python program to get the smallest number from a list.


def mySmall(l):
    if len(l) == 0:
        return 'The list is empty'
    smallest = l[0]
    for v in myList:
        if smallest > v:
            smallest = v
    return smallest


myList = [1, 2, 3, 4, 5]
sumRes = mySum(myList)
multRes = myMult(myList)
largeRes = myLarge(myList)
smallRes = mySmall(myList)

print(sumRes, multRes, largeRes, smallRes)
