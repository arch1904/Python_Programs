# Reverse Dictionary
#
# Given a dictionary, return a new dictionary with keys and values swapped.
#
# Example(s)
# ----------
# Example 1:
#   Input: {'a': 1, 'b': 2}
#   We will need to swap the keys and values.
#   Output:
#   {1: 'a', 2: 'b'}
#
# Parameters
# ----------
# d : dict
#   The dictionary you will be required to swap
#
# Returns
# -------
# dict
#   The dictionary given, but reversed
#
def reverse_dictionary(d):
    """
    Given a dictionary d, reverse the keys and values.
    """
    d2={} #New Empty Dictionary
    for k in d: # Iterating Through Keys in Dictionary
        d2[d[k]]=k #Assigning Former Value As Key and Former Key As Value
    return d2