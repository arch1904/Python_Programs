# Unique Rows
#
# Write a function that, given a 2d array (matrix) returns only the unique rows
# within a matrix, in the order that they appeared in the original matrix.
#
# 1 0 0 1 3
# 1 2 3 4 5     1 0 0 1 3
# 5 3 6 2 3  -> 1 2 3 4 5
# 1 0 0 1 3     5 3 6 2 3
# 5 3 6 2 3
#
# Example(s)
# ----------
# Example 1:
#   Input: [[1,2],[3,4],[1,2],[5,6]]
#   Output:
#   [[1,2],[3,4],[5,6]]
#
# Example 2:
#   Input: [[1,0,0,1,3],[1,2,3,4,5],[5,3,6,2,3],[1,0,0,1,3],[5,3,6,2,3]]
#   Output:
#   [[1,0,0,1,3],[1,2,3,4,5],[5,3,6,2,3]]
#
# Parameters
# ----------
# matrix : List[List]
#   A 2d array of arbitrary rectangular size with arbitrary data elements
#
# Returns
# -------
# List[List]
#   Returns a new matrix with the unique rows of the original matrix
#
def unique_rows(matrix):
    """
    returns unique rows
    """
    unique=[]#creates a new list to hold unique rows
    for l in matrix:
        if l in unique: #check if current row already exists in unique
            continue
        else:
            unique.append(l) #if its unique then add to unique list
    return unique
