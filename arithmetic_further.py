def add(list_1):
    total = 0
    for number in list_1:
        total += number
    print total

add([1, 2, 3, 4])

def subtract(list_1):
    total = list_1[0]
    for i in range(1, len(list_1)):
        total -= list_1[i]
    print total

subtract([10, 2, 3, 4])


def multiply(list_1):
    total = 1
    for number in list_1:
        total *= number
    print total

multiply([2, 1, 2, 0, 1])

def divide(list_1):
    total = list_1[0]
    for i in range(1, len(list_1)):
        total /= list_1[i]
    print total

divide([5,1,5])

def square(list_1):
    print list_1[0] ** 2

square([3])

def cube(list_1):
    print list_1[0] ** 3

cube([2])

def power(list_1):
    total = list_1[0]
    for i in range(1, len(list_1)):
        total **= list_1[i]
    print total

power([2, 3, 2])

def mod(list_1):
    print list_1[0] % list_1[1]
    

mod([5,2,5])
