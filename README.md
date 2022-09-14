# Nalios Dev test

You have 3 hours to do your first push in Git with what has been done. 

Important note : please try to be honest with the timing. You can still push afterwards within 24 hours if you want to enhance your code.

- If no precision is given, use Python 3 to answer these exercises.

- Take your time, breath, you can do the questions in any order. Read them carefully.

- Add a test case for each exercise, it's important for us to know how you test your code.

- If you don't know a full solution, you can explain what you wanted to do or do some pseudo code. Your logic will be taken into account.

- Do Bonus points of exercises once you finish everything, don't lose time on them.

- import this - if you know you know, else you'll know



## Ex 1: FizzBuzz

- Write a function that outputs numbers from 1 to 100 inclusive.

- If the number is a multiple of 3, print 'Fizz' instead

- If the number is a multiple of 5, print 'Buzz' instead

- If the number is a multiple of 3 AND 5, print 'FizzBuzz' instead

- Bonus point: make your function accept a dict parameter containing multiple words to output. So the program above would be

```python
yourfunction({
    '3': 'Fizz',
    '5': 'Buzz',
    '3/5': 'FizzBuzz' # or 3&5 or anything else if it matters to you :) 
})
```


## Ex 2: Game of Life

- Do you know the game of life ? You can find the rules here : https://playgameoflife.com (bottom left, Explanation, or if you need more precision, ask Google)

- Write a function that accepts a matrix in parameter and runs the Game of Life on it.

- Return the matrix after 5 iteration of the Game of Life.

- Bonus point: Just before returning the matrix, output it's result in HTML (don't need CSS, ugly stuff working is good)



## Ex 3: Hello, Nalios !

- In JavaScript, create a function that outputs "Hello, Nalios !"

- You can't use strings.



## Ex 4: PSQL

- Write pseudo-SQL statements to create database tables to store the products of a basic webshop. Each product has a name, a price, a creation date and may belong to several categories. Categories have a name and a flag to indicate whether the category is private or public.

- Write a SQL query to find the list of products that belong to more than 5 public categories



## Ex 5: MySum

- Write a function that takes an array of numbers in parameter (no joke : no None, no strings, only real numbers)

- Output the sum of these number, without using the sum() function.

- Bonus Point: Use recursion to get this sum



## Ex 6: Matrix Rotation

- Write a function that takes 3 parameters: a matrix, a number of rotations and the letter R or L (Right or Left)

- Output the matrix after it was rotated. Try to optimize your code as much as you can

- Example:
```python
matrix = [
    [1,2,3],
    [1,3,5],
    [1,4,7]
]
rotate_matrix(matrix, 1, 'L') # would output
[
    [3,5,7]
    [2,3,4]
    [1,1,1]
]
```


## Ex 7: OXO (Bonus after the 6 other ex., if you want to try it)

Write a small program that can play OXO game (so, within a 3x3 matrix, try to get three X or three O on the same line)
The def of your function should be def turn(game, symbol): game being the 3x3 matrix, symbol being 'O' or 'X'.
An empty cell has a dot (.) in it.
You can test your program against itself with this arena : https://github.com/pierrelocus/oxo_arena
ex. in random, but the goal is to implement the logic you have in your head
```python
from random import randint
def turn(game, symbol):
    # My symbol is symbol, the enemy is the opposite (so if I'm "X" he's "O")
    # I check in the matrix if he could win and block him
    # Else I try to get my symbol on the same line to win
    while 1:
        x = randint(0,2)
        y = randint(0,2)
        if game[x][y] == '.':
            game[x][y] = symbol
            return game
```