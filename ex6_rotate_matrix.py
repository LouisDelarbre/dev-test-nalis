import copy


def size_matrix(matrix):
    row = len(matrix)
    cols = len(matrix[0])
    return (row,cols)


def rotate_matrix_once(matrix,direction):
    size_matrix_var = size_matrix(matrix)
    
    #switching number of column and rows because it's doing it for each rotation
    new_matrix = [[0 for j in range(size_matrix_var[0])] for i in range(size_matrix_var[1])]



    for index_i,i in enumerate(matrix):
        for index_j,j in enumerate(i) :                
            if direction == "R":
                new_matrix[index_j][(size_matrix_var[0]-1)-index_i] = matrix[index_i][index_j]
            elif direction == "L":
                new_matrix[(size_matrix_var[1]-1)-index_j][index_i] = matrix[index_i][index_j]
    return(new_matrix)


def rotate_matrix(matrix, num_rotation, direction):
    # to avoid useless rotation ( 4 * 90 = 360, so each 4 rotation means the final matrix is the same than the beginning)
    num_rotation = num_rotation%4
    
    if num_rotation != 0:
        for _ in range(num_rotation):
            matrix = rotate_matrix_once(matrix,direction)

    print(matrix)
        




if __name__ == '__main__':
    matrix = [
        [1,2,3,4,5],
        [1,3,5,8,6],
        [1,4,7,9,7],
    ]

    rotate_matrix(matrix,3, "L")