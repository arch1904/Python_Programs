# Pascal's Triangle
#
# Write a function that, given an index i, returns the i'th row of Pascal's
# Triangle.
#
# This Wikipedia page on Pascal's triangle may be useful:
#   https://en.wikipedia.org/wiki/Pascal%27s_triangle
#
# Your solution should run in O(i) time and use O(i) space.
#
# Example(s)
# ----------
# Example 1:
#   Input: 2
#   Output: [1,2,1]
#
# Example 2:
#   Input: 6
#   Output: [1,6,15,20,15,6,1]
#
# Parameters
# ----------
# i : int
#   The row index of the row of Pascal's Triangle you are searching for
#
# Returns
# -------
# List[int]
#   Returns the i'th row of Pascal's Triangle as a list of ints
#
def pascals_triangle(i):
    '''
    returns i'th row of Pascal's Triange as a list of ints
    '''
    if i<0: #The Row Number cannot be negative
        return None
    row = [1] #First Element is always 1
    for col in range(1, i+1):
        row.append(row[len(row)-1] * (i+1 - col) / col) #calculates the current element in i'th row
    return row