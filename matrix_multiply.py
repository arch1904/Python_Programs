# matrix multiply
#
# Given two 2d arrays, return the product of those two matricies.
# You can read about matrix multiplication here: https://en.wikipedia.org/wiki/Matrix_multiplication
# If matrix multiplication is possible, return the product as a list representing said matrix.
# Otherwise, return None.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: [[1,4,6]], [[2,3],[5,8],[7,9]]
#
#
#   Output:
#   [[64,89]]
#
#   Reasoning:
#   Matrix product. Notice that the input and output for a matrix with one row is still nested in a 2d array.
#
# Parameters
# ----------
# arr0 : list
#   a 2d array representing a matrix
#
# arr1 : list
#   a 2d array representing a matrix
#
# Returns
# -------
# arr
#   2d array with the product
# None
#   if product is impossible
def matrix_multiply(arr0, arr1):
    """
    returns the product of two matricies, None if not possible.
    """
    if len(arr0[0])==len(arr1): #check to see if matrices are multiplied
    # matrice with no of rows equal to rows of first and columns = columns of second array
        multiplied=[[0 for i in range(len(arr1[0]))] for i in range(0,len(arr0))]
        #loop through all three lists and matrix multiply
        for i in xrange(len(arr0)):
            for j in xrange(len(arr1[0])):
                for k in xrange(len(arr0[0])):
                    multiplied[i][j] += arr0[i][k] * arr1[k][j]
        return multiplied

    else:
        # if matrices are not multipliable
        return None