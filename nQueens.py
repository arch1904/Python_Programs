# nQueens
#
# NQueens is a classical problem that asks if we can place N queens on an NxN chessboard so that no two queens can attack
# each other.
# Write a function nQueens(board) that takes a 2d array of bits (0 or 1) that indicates whether a queen is present on
# said tile (1 means the queen is present, 0 is an empty cell). Return boolean True if the configuration makes it so that
# none of the queens can attack each other, and false if there are any sets of Queens that can.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: [[0,1,0],[0,0,0],[0,0,1]]
#
#
#   Output:
#   True
#
#   Reasoning:
#   The queens are located in arr[0][1] and arr[2][2]. There is no straight path from either Queen to the other, therefore
#   they cannot attack each other.
#
# Parameters
# ----------
# arr : list
#   A 2d list/array of integers (0 or 1).
#
# Returns
# -------
# Bool
#   Whether or not any set of queens can attack eath other on the board
def nQueens(arr):
    """
    Returns if given array represents an nQueens configuration
    """
    for i in xrange(0,len(arr)):
        for j in xrange(0,len(arr[0])):
            if arr[i][j]==1:
                #check if any queen in same row,column or diagonal
                if row_check(arr,i,j) or column_check(arr,i,j) or diagonal_check(arr,i,j):
                    return False
    return True

def row_check(arr,row,column):
    """
    checks if there is a queen in the row of the current queen
    """
    for i in xrange(0,len(arr)):
        if i!=row: #excludes current queen
            if arr[i][column]==1:
                return True
def column_check(arr,row,column):
    """
    checks if there is a queen in the column of the given queen
    """
    for i in xrange(0,len(arr[row])):
        if i!=column: #excludes current queen
            if arr[row][i]==1:
                return True
def diagonal_check(arr,row,column):
    """
    checks if there is a queen on any possible diagonal of the given queen
    """
    i=row+1
    j=column+1
    k=row-1
    l=column-1
    while  i<len(arr) or j<len(arr[0]) or k>=0 or l>=0:
        if i<len(arr) and j<len(arr):
            if arr[i][j] ==1: #checks for element below and on the right
                return True
        elif k>=0 and l>=0:
            if arr[k][l]==1: #check for element above and on the left
                return True
        elif i<len(arr) and l>=0:
            if arr[i][l] == 1: #checks for element below and on the left
                return True
        elif k>=0 and j<len(arr):
            if arr[k][j] == 1: #checks for element above and on the right
                return True
        i+=1
        j+=1
        k-=1
        l-=1
    return False
