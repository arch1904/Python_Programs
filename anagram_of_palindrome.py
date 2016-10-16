from collections import defaultdict
# Anagram of Palindrome
#
# Given a string, find out if it is an anagram of a palindrome.
#
# Example(s)
# ----------
# Example 1:
#   Input: 'ivicc'
#   Output: True
#   Anagram of 'civic', which is a palindrome.
#
# Parameters
# ----------
# arg1 : String
#   Input String
#
# Returns
# -------
# bool
#   True if the string is an anagram of a palindrome, False otherwise
#
def anagram_of_palindrome(word):
    """
    Given a string, return true if the string is an anagram of a palindrome.
    """
    word=word.lower() #change string to lower case
    newdict = defaultdict(int) #declare default dictionary with type int
    for c in word:
        newdict[c] += 1
    times = 0
    for i in newdict.values(): #parse through newdict values and check times
        if times == 2:
            return False
        if i == 1:
            times += 1
    return True