# Count Vowels
#
# For our purposes a vowel is either a, e, i, o, or u. Iterate through
# a string and return the number of vowels in it. Case does not matter.
#
# Example(s)
# ----------
# Example 1:
#   Input: aAaeeizzzzz
#   This string contains 3 a's, 2 e's, 1 i. So 5 vowels.
#   Output:
#   5
#
# Parameters
# ----------
# str_in : str
#   A mixed case single line string.
#
# Returns
# -------
# int
#   Number of vowels.
#
def count_vowels(str_in):
    vowels=['a','e','i','o','u']
    count=0
    str_in=str_in.lower()
    for c in str_in:
        if c in vowels:
            count+=1
        else:
            pass
    return(count)