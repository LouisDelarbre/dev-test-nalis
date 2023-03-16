import random


len_list = 15
list_num = []

#creating the random list with n elements ( n = len_list)
for i in range(len_list):
    number = random.randint(1,100)
    list_num.append(number)

#check if the list is composed with number and nothing else
def is_array_number(list_numbers):
    if isinstance(list_numbers, list) and all(isinstance(number, int) for number in list_numbers):
        return True
    else:
        return False

#recursive funct to have the sum from list_numbers
def my_sum(list_numbers):
    if len(list_numbers) > 0:
        return list_numbers[-1] + my_sum(list_numbers[:-1])
    else :
        return 0
        


if __name__ == '__main__':
    #print to see the list a first time
    print(list_num)

    print(f'Final sum = {my_sum(list_num)}')