import copy


def rotate_matrix_once(matrix,direction):
    new_matrix = copy.deepcopy(matrix)

    lng_mat = len(matrix) - 1
    for index_i,i in enumerate(matrix):
        for index_j,j in enumerate(i) :                
            if direction == "R":
                new_matrix[index_j][lng_mat-index_i] = matrix[index_i][index_j]
            elif direction == "L":
                new_matrix[lng_mat-index_j][index_i] = matrix[index_i][index_j]
    return(new_matrix)


def rotate_matrix(matrix, num_rotation, direction):
    
    for _ in range(num_rotation):
        matrix = rotate_matrix_once(matrix,direction)

    print(matrix)
        
        

matrix = [
    [1,2,3],
    [1,3,5],
    [1,4,7]
]
rotate_matrix(matrix,1, "L")