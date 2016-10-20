# String, My One True Love
#
# Your favorite course staff member really likes strings that have the same occurances of letters.
# This means the staff member likes "aabbcc" and "ccddee" and even strings like "abcabcabc"
#
# But "that one guy that wrote the pokomon problem" wants to trick the staff with really long string,
# that either could be the string that the staff member likes, or something that becomes such a string
# when you remove a single character from the string.
#
# Your goal is to return True if it's a string that the "one guy that wrote the pokomon problem" made
# and False otherwise.
#
# Restrictions
# ------------
# Inputs are only given as lower case alphabets, without punctuation, spaces, etc.
# Your solution must run in O(n) time.
#
# Example(s)
# ----------
# Example 1:
#   Input: "abcbabcdcdda"
#   There is 3 a's, 3 b's, 3 c's, and 3 d's. That means it is a very likable string!
#   Output:
#   True
#
# Example 2:
#   Input: "aaabbbcccddde"
#   Again there are 3 a's, 3 b's, 3 c's, and 3 d's. However, we also have 1 e!
#   We can remove this string however, and it will become a likeable string, so this is valid.
#   Output:
#   True
#
# Example 3:
#   Input: "aaabbbcccdddeeffgg"
#   This string is similar to the other ones, except with 2 e's, f's and g's at the end.
#   To make this string likable, we need to remove the 2 e's, f's, and g's or we can remove
#   one a, b, c, and d. However all of these require more than one removal, so it becomes invalid.
#   Output:
#   False
#
# Parameters
# ----------
# string : str
#   The string to check whether it is likeable or not.
#
# Returns
# -------
# bool
#   True if the string is likable, or removing a single character makes it likable.
#   False if the string is not likeable, and we need to remove more than 1 character to become likable.
def string_my_one_true_love(string):
    '''
    returns True if a string is likable or removing a single character makes it likable
    '''
    count_alpha={} #Empty Dictionary
    minimum=0 # holds the minimum count
    no_of_ones=0 
    for i in xrange(0,len(string)):
        if string[i] in count_alpha: #if char already in dict increase occurence by 1
            count_alpha[string[i]]+=1
        else:
            count_alpha[string[i]] =1 #else initialise it to 1

    minimum=min(count_alpha.values())

    for c in count_alpha:
        if count_alpha[c]%minimum>1: # If count of any character is off by more than 1 from minimum then the string is not likable
            return False
        if abs(count_alpha[c]-minimum) ==1: 
            no_of_ones+=1 #no of chars which may have to be removed

    if no_of_ones ==0 or no_of_ones ==1: #If no chars have to be removed or only one has to be removed
        return True
    return False
