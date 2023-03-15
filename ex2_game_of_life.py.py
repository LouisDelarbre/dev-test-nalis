import random
import copy


#number of step
steps = 5
matrix_row = 5
matrix_col = 5

def create_matrix(row, column):

    matrix = [[random.randint(0, 1) for _ in range(column)] for _ in range(row)]
    return matrix

#check if it's a matrix
def is_matrix(matrix):
    if isinstance(matrix, list) and all(isinstance(row, list) for row in matrix):
        return True
    else:
        return False


def get_cell(i,j, matrix):
    if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
        return matrix[i][j]



def game_of_life(matrix):
    if not is_matrix(matrix):
        print("please give a correct matrix as parameter")
        return
    new_matrix = copy.deepcopy(matrix)
    for row in range(len(matrix)):
        for column in range(len(matrix[row])) :
            cell = get_cell(row,column, matrix) 
            neihbours = 0

            if get_cell(row, column-1,matrix) == 1 : neihbours +=1
            if get_cell(row, column+1,matrix) == 1 : neihbours +=1
            if get_cell(row-1, column,matrix) == 1 : neihbours +=1
            if get_cell(row+1, column,matrix) == 1 : neihbours +=1
            if get_cell(row-1, column-1,matrix) == 1 : neihbours +=1
            if get_cell(row-1, column+1,matrix) == 1 : neihbours +=1
            if get_cell(row+1, column-1,matrix) == 1 : neihbours +=1
            if get_cell(row+1, column+1,matrix) == 1 : neihbours +=1

            if neihbours == 0 or neihbours == 1:
                new_matrix[row][column]= 0
            elif neihbours >= 4:
                new_matrix[row][column]= 0
            elif cell == 1 and (neihbours == 2 or neihbours == 3):
                new_matrix[row][column]= 1
            elif cell == 0 and neihbours == 3:
                new_matrix[row][column]= 1
            else :
                new_matrix[row][column]= 0
    return new_matrix
    






matrix = create_matrix(matrix_row,matrix_col)
print(matrix)

for i in range(steps):
    matrix = game_of_life(matrix)

print(matrix)
