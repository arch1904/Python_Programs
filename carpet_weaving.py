###############################################################################
# Carpet Weaving
#
# Given a width and height, print out a carpet design with alternating diagonal rows of O's and X's
# Define and use a helper function to decide if a carpet square should be an O or X.
#
# Example(s)
# ----------
# Example 1:
#   Input: 4,3
#   Width of 4 and height of 3
#   Output:
#   XOXO
#   OXOX
#   XOXO
#
# Example 2:
#   Input: 2,2
#   Width of 2 and height of 2
#   Output:
#   XO
#   OX
#
# Parameters
# ----------
# width : int
#   Width of carpet
# height : int
#   Length of carpet
#
# Prints
# -------
# The finished carpet
#
def weave_carpet(width, height):
    """
    Prints a design width alternating diagonal rows of O's and X's
    Must use a helper function

    >>> weave_carpet(2,3)
    XO
    OX
    XO
    """
    # Your code goes here!
    for i in range(0,height):
        str1=""
        for j in range(0,width):
            if (i+j)%2==0:
                str1=str1+"X"
            else:
                str1=str1+"O"
        print(str1)