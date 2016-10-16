# Pangram
#
# A pangram is any string that contains all the letters of the alphabet.
# In this function, you will be given a string and your task is to RETURN
# a boolean representing whether or not the string is a pangram.
#
# Note: Case does not matter when determining if a string is a pangram. So,
#       'abcDeFghiJkLmNopqrstuvwxyz' is a valid pangram.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: 'the quick brown fox jumps over the lazy dog'
#   This string indeed contains all letters from a-z
#   Output:
#   True
#
# Parameters
# ----------
# str_in : str
#   A mixed case single-line string.
#
# Returns
# -------
# bool
#   Whether or not str_in is a pangram
#
def pangram(str_in):
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    flag=0
    str_in=str_in.lower()
    for c in alphabet:
        if c in str_in:
            pass
        else:
            flag=1
    if flag==1:
        return(False)
    elif flag==0:
        return(True)