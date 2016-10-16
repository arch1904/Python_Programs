# Unique
#
# Check if a word is made up of unique letters
# Note: Case does not matter
#
# Example(s)
# ----------
# Example 1:
#   Input: 'computer'
#   The word 'computer' has no repeating letters
#   Output:
#   True
#
# Example 2:
#   Input: 'science'
#   The word 'science' repeats the letters c and e
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
#   Whether or not str_in is made up of unique letters
#
def unique(str_in):
    flag=0
    for i in range(0,len(str_in)):
        for j in range(i+1,len(str_in)):
            if str_in[i].lower()==str_in[j].lower():
                flag=1
            else:
                pass
    if flag==0:
        return(True)
    else:
        return(False)