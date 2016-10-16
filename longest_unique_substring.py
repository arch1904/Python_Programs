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
    i, j = 0, 0
    I, J = 0, 0
    word1=word.lower()
    H = set([])
    while j < len(word1):
        if word1[j] in H:
            H.remove(word1[i])
            i += 1
        else:
            H.add(word1[j])
            j += 1
        if J - I < j - i:
            I, J = i, j
    return word[I:J]