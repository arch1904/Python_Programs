# Most Common Character
#
# You will receive a string as a parameter and you will need to return the
# character in the string that occurs the most. Case does not matter. The
# output should be lower case (if applicable). In case of a tie, return the
# character that showed up first.
#
# Example(s)
# ----------
# Example 1:
#   Input: aaAAaBBbcc
#   a occurs the most, at 5 times.
#   Output:
#   a
#
#
# Parameters
# ----------
# str_in : str
#   A mixed case single line string
#
# Returns
# -------
# str
#   The most common character in the given string
#
def most_common_char(str_in):
    maxchar=''
    max_count=0
    for i in range(0,len(str_in)):
        count=0
        for c in str_in.lower():
            if c==str_in[i].lower():
                count+=1
        if count>max_count:
            max_count=count
            maxchar=str_in[i].lower()
        else:
            pass
    return(maxchar)