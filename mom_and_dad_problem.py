###############################################################################
# Mom and Dad
#
# Given a string, RETURN True if the continous substring 'mom' appears the same number of times
# as the continous substring 'dad'. Otherwise, RETURN false.
#
# The input will always be given as a lower case string. You do not have to worry about upper cases.
#
# Example(s)
# ----------
# Example 1:
#   Input: mom_and_dad('momdad')
#   We have the substring going from 'mom' and 'dad'. There is one each.
#
#   Output:
#   True
#
# Example 2:
#   Input: mom_and_dad('momomdad')
#   We have the string 'mom' from the first part of the string (mom omdad)
#   However, we have another occurance of 'mom' right after. (mo mom dad)
#   Next we only have 1 occurance of 'dad'.
#
#   Output:
#   False
#
# Parameters
# ----------
# string: String
#   String representing the sentence to find the number of occurances of 'mom' and 'dad'.
#   The string will always be given as a lowercase.
#
# Returns
# -------
# Bool
#   Boolean representing whether or not the same number of 'mom' and 'dad' occur in the string.
def mom_and_dad(string):
    """
    Given a string, RETURN True if the number of appearnces of 'mom' and 'dad' are the same.

    >>> mom_and_dad('momdad')
    True
    >>> mom_and_dad('momomdad')
    False
    >>> mom_and_dad('mom091213aiomomdadmomoomomomdadadfishsdadandwich')
    False
    >>> mom_and_dad('momomdadad')
    True
    """
    # Your code goes here!
    dad_count=0
    mom_count=0
    for i in range(0,len(string)-2):
        if string[i]+string[i+1]+string[i+2]=="mom":
            mom_count+=1
        elif string[i]+string[i+1]+string[i+2]=="dad":
            dad_count+=1
    if dad_count==mom_count:
        return True
    else:
        return False