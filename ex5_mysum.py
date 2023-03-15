import random

list_num = []

#creating the random list
for i in range(10):
    number = random.randint(1,100)
    list_num.append(number)

def is_array_number(list_numbers):
    if isinstance(list_numbers, list) and all(isinstance(number, int) for number in list_numbers):
        return True
    else:
        return False

def my_sum(list_numbers):
    #print to see the list a first time
    print(list_numbers)
    sum = 0
    for i in list_numbers:

        sum += i

    return sum


print(my_sum(list_num))