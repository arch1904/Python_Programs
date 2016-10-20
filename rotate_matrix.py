# Rotate Matrix
#
# Write a function that given an NxN matrix will rotate the matrix to the left 90 degrees
#
# Examples
# ----------
# Example 1:
#   Input: [[1,2],[3,4]]
#   Output: [[2,4],[1,3]]
#
# Example 2:
#   Input: [[1,2,3],[4,5,6],[7,8,9]]
#   Output: [[3,6,9],[2,5,8],[1,4,7]]
#
# Parameters
# ----------
# matrix: List[List[int]]
#   A square matrix of ints
#
#
# Returns
# -------
# List[List[int]]
#   Returns parameter matrix rotated 90 degrees to the left
#
def matrix_transpose(matrix):
    """
    returns the matrix transpose
    """
    # create a list with no of rows = no of columns in original and vice versa
    transpose= [[0 for y in range(len(matrix))] for x in range(len(matrix[0]))]
    #loop through the new array
    for i in xrange(0,len(matrix[0])):
        for j in xrange(0,len(matrix)):
            transpose[i][j]=matrix[j][i] #reverse rows and columns and add to new array
    return transpose
def rotate_matrix(matrix):
    '''
    returns a matrix rotated by 90 degrees to the left
    '''
    #We Know Matrix Rotates by 90 degrees by left by taking transpose and then reversing all columns
    matrix=matrix_transpose(matrix) #Transpose the matrix
    for i in xrange(0,len(matrix[0])):
        for j in xrange(0,len(matrix)/2):
            matrix[j][i],matrix[len(matrix)-1-j][i]=matrix[len(matrix)-1-j][i],matrix[j][i] #Reverse Columns Of Transposed Matrix
    return matrix