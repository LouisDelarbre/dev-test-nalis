import random

# Exercise 1 

def fizzbuzz(number):
    if number % 3 == 0 or number % 5 == 0:
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")


#create list with random number between 0 and 100
random_numbers = []
for i in range(10):
    number = random.randint(1,100)
    random_numbers.append(number)

fizzbuzz(random_numbers)


