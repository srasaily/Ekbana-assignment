import numpy as np
from numpy import random


def eigen_transformation(matrix1, matrix2, transformation_matrix):
    '''
    solution for question 1 entry point
    :param matrix1: input matrix1
    :param matrix2: input matrix2
    :param transformation_matrix: transformation matrix
    :return: list of dictionary if success
    '''
    matrix1_rows, matrix1_column = matrix1.shape
    matrix2_rows, matrix2_column = matrix2.shape
    max_eigen_value = None
    try:
        if matrix1_rows == matrix1_column and matrix2_rows == matrix2_column:
            matrices_list = [matrix1, matrix2]
            result_list = []
            for matrix in matrices_list:
                # arbitrary eigen value
                eigen_value = 2

                # random eigen vectors
                eigen_vector = random.randint(1,10,(matrix.shape[0],1))
                old_eigen_vector = random.randint(1,10,(matrix.shape[0],1))

                while not compare_vectors(eigen_vector, old_eigen_vector):
                    old_eigen_vector = eigen_vector
                    eigen_vector = matrix_multiplication(matrix, eigen_vector)
                    if eigen_vector is None:
                        raise Exception('Cannot get eigen vector')
                    max_eigen_value = eigen_vector.max()
                    eigen_vector = eigen_vector/max_eigen_value
                    eigen_vector = eigen_vector.round(2)

                eigen_value = max_eigen_value
                eigen_value = round(eigen_value, 2)

                transformation_vector = matrix_multiplication(transformation_matrix, eigen_vector)
                if transformation_vector is not None:
                    transformation_vector = transformation_vector.round(2)

                eigen_dict = {"eigenvalue": eigen_value,
                                "eigenvector": eigen_vector,
                                "transformationvector": transformation_vector}

                result_list.append(eigen_dict)
            return result_list
    except Exception as ex:
        print('Error. Could not calculate. {}'.format(ex))
        return None


def matrix_multiplication(matrix_a, matrix_b):
    '''
    multiplies two matrices
    :param matrix_a: input matrix a
    :param matrix_b: input matrix b
    :return: product of matrix a and b
    '''
    result_matrix = np.ones((matrix_a.shape[0], matrix_b.shape[1]))
    try:
        if matrix_a.shape[1] != matrix_b.shape[0]:
            return None

        for i in range(matrix_a.shape[0]):
            for j in range(matrix_b.shape[1]):
                sum = 0
                for k in range(matrix_b.shape[0]):
                    sum += matrix_a[i,k] * matrix_b[k,j]

                result_matrix[i,j] = sum
        return result_matrix

    except Exception as ex:
        print('Error. Could not multiply matrices. {}'.format(ex))
        return None


def compare_vectors(vector1, vector2):
    '''
    compare two vectors
    :param vector1: input vector1
    :param vector2: input vector2
    :return: true if vector 1 is equal to vector2 else false
    '''
    is_equal = False
    try:
        for row_index in range(vector1.shape[0]):
            if vector1[row_index,0] == vector2[row_index,0]:
                is_equal = True
            else:
                is_equal = False
                break
    except Exception as ex:
        print('Error. Could not compare vectors. {}'.format(ex))
    return is_equal


def get_transformation_matrix():
    input_matrix = []
    for i in range(3):
        if i == 2:
            print("Dimension for rectangular matrix")
        else:
            print("Dimension for square matrix {}".format(i))
        rows = int(input("Enter number of rows:"))
        if i == 2:
            column = int(input("Enter number of column:"))
        else:
            column = rows
        mat = np.zeros((rows,column))
        print("Enter matrix element:")
        for row_element in range(rows):
            for column_element in range(column):
                mat[row_element][column_element] = float(input("{}{}:".format(row_element, column_element)))
        input_matrix.append(mat)
    return input_matrix


if __name__ == '__main__':
    input_matrices = get_transformation_matrix()
    print(str(eigen_transformation(input_matrices[0], input_matrices[1], input_matrices[2])))
