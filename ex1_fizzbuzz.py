import random

# Exercise 1 
quantity_number_to_create = 20
carachter_splitter = "/"
rules_dict = {
    '3': 'Fizz',
    '5': 'Buzz',
    '3/5': 'FizzBuzz', # or 3&5 or anything else if it matters to you :) 
    # '4' : "Vroum" 
    }

def parse_to_int(value):
    return value.split(carachter_splitter)


def fizzbuzz(numbers):
    for number in numbers:

        # print(number)
        list_to_print = []
        value_to_print = ([],0)
        for key,value in rules_dict.items():
            switch_rule = True
            key_parsed = parse_to_int(key)
            for i in key_parsed:
                if number % int(i) == 0:
                    list_to_print.append(i)
                    switch_rule = True
                else :
                    switch_rule = False
                    break
            if switch_rule:
                #if we are not sure about the order we loop and want to take the "biggest" combinaison of number we can add the function below :
                # if len(key_parsed) > len(value_to_print[0]):
                value_to_print = (key_parsed, value)


        if value_to_print[0] != []:
            print(value_to_print[1])





#create list with random number between 1 and 100
random_numbers = []
for _ in range(quantity_number_to_create):
    number = random.randint(1,100)
    random_numbers.append(number)

if __name__ == '__main__':
    print(random_numbers)
    fizzbuzz(random_numbers)


