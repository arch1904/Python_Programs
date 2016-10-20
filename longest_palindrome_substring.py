# Longest Palindromic Substring
#
# Given a string, find the longest substring that is a palindrome. If
#
# Ideal runtime: o(n), but we will give full credit for o(n^2) solutions.
#
# RESTRICTIONS:
# There is guarunteed to be exactly 1 longest palindrome
#
# Example(s)
# ----------
# Example 1:
#   Input: "ABBAC"
#
#   Output:
#   "ABBA"
#
# Example 2:
#   Input: "A"
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
#    Longest Palindrome substring
def longest_palindrome_substring(word):
    '''
    returns longest palindromic substring
    '''
    if len(word)==1: #if length of a word is just one the word is the longest palindromic substring
        return word
    all_palindromes = [] #Empty List to contain all palindromes inside the string
    for i in range(len(word)):
        for j in range(0, i):
            substr = word[j:i + 1] #Get a substring from the string
            if substr.lower() == substr[::-1].lower(): #checks if a substring is a palindrome
                all_palindromes.append(substr)
    return max(all_palindromes,key=len)# Returns palindrome with the max length