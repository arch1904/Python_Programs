# Matrix Transpose
#
# Write a function that, given a 2d array (matrix) returns the trasnpose
# of that matrix. The transpose of a matrix is when the rows of the
# source matrix become the columns of the resulting matrix:
#
# 1  2      1  3  5
# 3  4  ->  2  4  6
# 5  6
#
# It may be useful to read this Wikipedia article on matrix transposes:
#   https://en.wikipedia.org/wiki/Transpose
#
# Note: You may not use any builtin functions in this problem.
#
# Example(s)
# ----------
# Example 1:
#   Input: [[1,2],[3,4],[5,6]]
#   Output:
#   [[1, 3, 5], [2, 4, 6]]
#
# Example 2:
#   Input: [['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p']]
#   Output:
#   [['a', 'e', 'i', 'm'], ['b', 'f', 'j', 'n'], ['c', 'g', 'k', 'o'], ['d', 'h', 'l', 'p']]
#
# Parameters
# ----------
# matrix : List[List]
#   A 2d array of arbitrary rectangular size with arbitrary data elements
#
#
# Returns
# -------
# List[List]
#   Returns the transposed matrix
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