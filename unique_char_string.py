# is unique
#
# Given a string, find out if it is made of only unique characters. Characters are not case sensitive,
# so 'l' and 'L' are considered to be the same character.
#
# Example(s)
# ----------
# Example 1:
#   Input: 'abcdef'
#   Output: True
#   'abcdef' is made of unique characters
#
# Example 2:
#   Input: 'hello worLd'
#   Output: False
#   There are 3 'l's in 'hello world', therefore it is not made of unique characters.
#
#
# Parameters
# ----------
# arg1 : String
#   Input String
#
# Returns
# -------
# bool
#   True if the string is made of unique characters, false otherwise.
#
def is_unique(word):
    """
    Given a string, return true if the string is made of unique characters.
    """
    char_mapping=char_dict_mapping()
    in_list=[] #empty list to hold value of character that has already appeared
    word=word.lower()
    for c in word:
        if char_mapping[c] in in_list: #if even single char repeats, False
            return False
        else:
            in_list.append(char_mapping[c]) #add appearing character mapping to list
    return True
