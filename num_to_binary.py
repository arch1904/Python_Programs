###############################################################################
# To_Binary
#
# RETURN a string representing the integer parameter in binary.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: 23
#   The binary representation of 23 is 10111
#   Output:
#   '10111'
#
# Parameters
# ----------
# num : integer
#   A positive integer
#
# Returns
# -------
# str
#   String representation of the integer using the fewest number of characters
#   as possible. (No zero padding)
#
def to_binary(num):
    """
    Represents an integer in binary as a string of 0's and 1's

    >>> print to_binary(23)
    10111
    >>> print to_binary(123456789)
    111010110111100110100010101
    """
    # Your code goes here!
    bin1=""
    temp=""
    r=0
    while(num>=1):
        r=num%2
        if num==1:
            num=0
        else:
            num=num/2
        temp=temp+str(r)
    for i in range (len(temp)-1,-1,-1):
        bin1=bin1+temp[i]
    return bin1