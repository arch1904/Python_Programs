###############################################################################
# Sum List
#
# Return an integer that represents the sum of the string list
#
#
# Example(s)
# ----------
# Example 1:
#   Input: "20,4,12"
#   The summation of 20, 4, and 12 is 36.
#   Output:
#   36
#
# Parameters
# ----------
# nums : str
#   Comma separated string list of integers
#
# Returns
# -------
# int
#   Int representation of the sum of strings from the list
#
def sum_list(arr):
    """
    Sums the list of strings into an int

    >>> print sum_list("1,2,3,4")
    10
    >>> print sum_list("4,4")
    8
    """
    # Your code goes here!
    arr=arr.split(",")
    sum=0
    for i in arr:
        sum=sum+int(i)
    return(sum)