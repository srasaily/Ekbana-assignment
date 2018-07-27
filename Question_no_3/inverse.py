import numpy as np


def inverse(matrix):
    '''
    returns the inverse matrix of input matrix
    :param matrix: input matrix
    :return: inverse of matrix
    '''
    rows, column = matrix.shape
    try:
        if rows == column:
            inverse_matrix = np.linalg.inv(matrix)
            return inverse_matrix
        else:
            print("Not a square matrix!")

    except Exception as ex:
        print("Error. Could not calculate inverse {}".format(ex))


def transpose(matrix):
    '''
    returns the transpose of input matrix
    :param matrix: input matrix
    :return: transpose of input matrix
    '''
    rows, column = matrix.shape
    transpose_matrix = np.zeros((column,rows))
    try:
        for rows_element in range(rows):
            for column_element in range(column):
                transpose_matrix[column_element, rows_element] = matrix[rows_element, column_element]
        return transpose_matrix
    except Exception as ex:
        print("Error. Could not calculate transpose. {}".format(ex))


def get_matrix():
    '''
    gets the elements of the a matrix
    :return: input matrix
    '''
    rows = int(input("Enter number of rows:"))
    column = int(input("Enter number of column:"))
    input_mat = np.zeros((rows,column))
    print("Enter matrix element:")
    for row_element in range(rows):
        for column_element in range(column):
            input_mat[row_element, column_element] = int(input("{}{} ".format(row_element,column_element)))
    return input_mat


if __name__ == "__main__":
    input_matrix = get_matrix()
    print("Inverse of the matrix:")
    print(inverse(input_matrix))
    print("Transpose of matrix:")
    print(transpose(input_matrix))