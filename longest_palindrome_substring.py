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
    if len(word)==1:
        return word
    all_palindromes = []
    for i in range(len(word)):
        for j in range(0, i):
            chunk = word[j:i + 1]
            if chunk.lower() == chunk[::-1].lower():
                all_palindromes.append(chunk)
    return max(all_palindromes,key=len)