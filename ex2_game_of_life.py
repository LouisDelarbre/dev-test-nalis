import random
import copy
import webbrowser
import os

my_origin_path = os.path.dirname(os.path.realpath(__file__)) 


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


#one step of game_of_life
def game_of_life(matrix):
    if not is_matrix(matrix):
        print("please give a correct matrix as parameter")
        return
    new_matrix = copy.deepcopy(matrix)
    for row in range(len(matrix)):
        for column in range(len(matrix[row])) :
            cell = get_cell(row,column, matrix) 
            neihbours = 0
            #checking all the neibours cases
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
    


# create one matrix in html
def create_html_matrix(matrix):
    html_matrix = '<table border="1" width="200" height="200">'
    for i in matrix:
        html_matrix += '<tr>'
        for j in i:
            if j == 0:
               html_matrix += '<td></td>'
            elif j == 1:
                html_matrix += '<td bgcolor="black"></td>'


        html_matrix += '</tr>'
    html_matrix += '</table>'
    return html_matrix



#create a final page in html and open it
def save_open_html(list_html):
    with open(my_origin_path+'/gameoflife.html','w') as f:

        message = f"""<html>
        <head></head>
        <body>
        <h1> Response with final Matrix </h1>:
        {html_array[-1]}
        <hr>
        <hr>
        <hr>
        <h1> Bellow, all the steps to have the final response : </h1>"""
        
        for index,i in enumerate(html_array):
            message += f"<h1>Matrix with step num {index} </h1>"
            message += i

        message += """
        </body>
        </html>"""

        f.write(message)
        f.close()


    
    filename = 'file://'+ my_origin_path + '/gameoflife.html'
    webbrowser.open_new_tab(filename)



if __name__ == '__main__':
    matrix = create_matrix(matrix_row,matrix_col)
    print(matrix)
    #we will append  the html_matrix to html_array 
    html_array = []

    # executing the game of life X time (number of steps)
    for _ in range(steps):
        html_array.append(create_html_matrix(matrix))
        matrix = game_of_life(matrix)
    html_array.append(create_html_matrix(matrix))
    
    save_open_html(html_array)

    print(matrix)
