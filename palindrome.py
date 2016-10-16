# Palindrome
#
# A palindrome is any string that is the same when reversed.
# You will be given a string and you must RETURN a boolean
# representing whether or not the string is a palindrome.
#
# Note: Case does not matter
#
#
# Example(s)
# ----------
# Example 1:
#   Input: 'a nut for a jar of tuna'
#   This string is the same forward and back
#   Output:
#   True
#
# Example 2:
#   Input: 'this is not a palindrome'
#   This string is not the same forward and back
#   Output:
#   False
#
# Parameters
# ----------
# str_in : str
#   A mixed case single-line string.
#
# Returns
# -------
# bool
#   Whether or not str_in is a palindrome
#
def palindrome(str_in):
    str1=''
    str_in=str(str_in)
    str_in=str_in.lower()
    for i in range(0,len(str_in)):
        if str_in[i].isalnum():
            str1=str1+str_in[i]
        else:
            pass
    str_in=str1
    for i in range(0,len(str_in)):
        char=str_in[i]
        if char != str_in[-i-1]:
            return False
    return True