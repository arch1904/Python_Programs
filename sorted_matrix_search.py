# Sorted Matrix Search
#
# Write a function that, given a square 2d array (matrix) of integers and a
# target integer, will return the 'coordinates' of the target integer as a
# tuple in the form (row, col) if the element exists in the matrix, or (-1, -1)
# if the element does not exists.
#
# The matrix is guaranteed to be sorted ascending row-wise, and the zeroth
# element of each row is strictly larger than the last element of the
# previous row.
#
# Your solution should run in O(logn) time.
#
# Example(s)
# ----------
# Example 1:
#   Input: [[1,2,3],[8,11,16],[23,24,25]], 8
#   Output:
#   (1, 0)
#
# Example 2: 
#   Input: [[1,2,3],[8,11,16],[23,24,25]], 20
#   Output:
#   (-1, -1)
#
# Parameters
# ----------
# matrix : List[List[int]]
#   A square 2d array of integers
#
# target : int
#   The target integer to search the matrix for
#
# Returns
# -------
# Tuple(int, int)
#   Returns (row, col) coordinates of the target, or (-1, -1) if the target
#   is not in the matrix
#
def find_row(matrix,target):
    ''' 
    binary search to find row which may contain target element
    '''
    j=len(matrix[0])-1
    upper =0
    lower=len(matrix)-1
    while upper<=lower:
        mid=(upper+lower)//2
        if matrix[mid-1][j]<target and matrix[mid][j]>=target:
            return mid
        elif matrix[mid][j]<target:
            upper=mid+1
        elif matrix [mid][j]>target:
            lower=mid-1
    return -1
def find_column_of_element_in_row(array,target):
    '''
    binary search to find element in the row found in find_row
    '''
    upper=0
    lower=len(array)-1
    while upper<=lower:
        mid=(upper+lower)//2
        if array[mid]==target:
            return mid
        elif array[mid]<target:
            upper=mid+1
        elif array[mid]>target:
            lower=mid-1
    return -1
def sorted_matrix_search(matrix, target):
    '''
    returns co-ordinates of a specific number in a 2d sorted matrix
    '''
    i=find_row(matrix,target)
    if i==-1: #If it isnt possible for the number to be a part of this matrix
        return -1,-1
    j=find_column_of_element_in_row(matrix[i],target)
    if j==-1: #if the number isnt in the matrix
        return (-1,-1)
    return (i,j)