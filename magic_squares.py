# Magic Squares
#
# A magic square is an arrangement of distinct integers in a grid, where the numbers in each row, column, and the main
# and secondary diagonals all add up to be the same number, called the "magic constant".
# Given a 2d array representing a grid, find out if it is a magic square. Return is boolean "True" or "False".
#
# Restrictions:
# You CANNOT assume the size of the square
# You CANNOT assume that your input IS a square
# you CAN assume that objects in the grid will only be integers.
#
# Example(s)
# ----------
# Example 1:
#   Input: [[2,7,6],[9,5,1],[4,3,8]]
#
#
#   Output:
#   True
#
#   Reasoning:
#   row 0: 2+7+6 = 15
#   row 1: 9+5+1 = 15
#   row 2: 4+3+8 = 15
#   col 0: 2+9+4 = 15
#   col 1: 7+5+3 = 15
#   col 2: 6+1+8 = 15
#   diag 1: 2+5+8 = 15
#   diag 2: 4+5+6 = 15
#
#
# Parameters
# ----------
# arr : list
#   A 2d list/array of integers.
#
# Returns
# -------
# Bool
#   Whether or not the 2d matrix represents a magic square.
def magic_square(arr):
    """
    Returns if given array represents a magic square
    """
    if len(arr)!=len(arr[0]):
        return False
    sum_diagonal=0
    sum_anti_diagonal=0
    sum_rows=0
    sum_columns=0
    for i in xrange (0,len(arr)):
        sum_rows+=sum(arr[i]) #get sum of all rows
        for j in xrange(0,len(arr[i])):
            if i==j:
                sum_diagonal+=arr[i][j] #sum of diagonal
            if i+j==len(arr)-1:
                sum_anti_diagonal+=arr[i][j] #sum of anti diagonal
            sum_columns+=arr[j][i] #get sum of all columns
    sum_columns/=len(arr) #sum of all columns divided by number of columns gives sum of one columns
    sum_rows/=len(arr) #sum of all rows divided by number of rows gives sum of one row
    #check if all sums are equal
    if sum_rows==sum_columns and sum_rows==sum_diagonal and sum_diagonal==sum_anti_diagonal:
        return True
    return False
