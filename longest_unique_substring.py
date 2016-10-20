# Longest Unique Substring
#
# Given a string, find the longest unique substring
#
# Ideal runtime: o(n). full credit only given for o(n).
#
# RESTRICTIONS:
# There is guarunteed to be exactly 1 longest unique substring
#
# Example(s)
# ----------
# Example 1:
#   Input: "asdfawefABCDEFaabasfeasf"
#
#   Output:
#   "wefABCDEF"
#
# Example 2:
#   Input: "AA"
#
#   Output:
#   "A"
#
# Parameters
# ----------
# word: str
#   String input
#
# Returns
# -------
# String
#    Longest unique substring
def longest_unique_substring(word):
    '''
    returns the longest unique substring
    '''
    i, j = 0, 0 
    previous_i,previous_j = 0, 0 #
    word1=word.lower()
    H = set([]) #create an empty set
    while j < len(word1):
        if word1[j] in H: #if the char at j is in the set
            H.remove(word1[i]) #remove the char
            i += 1 #increment i
        else:
            H.add(word1[j]) #If the word is not in the set then add it to the set
            j += 1 #increase j
        if previous_j - previous_i < j - i:
            previous_i, previous_j = i, j
    return word[previous_i:previous_j]