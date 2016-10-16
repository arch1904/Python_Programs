# Counting Anagrams
#
# Write a function that, given a string, will return the number of instances
# of anagrams of that string in the provided list of strings.
#
# Two strings are anagrams when they have the exact same number and frequency
# of characters, and order is ignored. Taking a string and rearranging its
# characters generates anagrams of that string. So, 'listen' and 'silent' are
# anagrams.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: ['19cs6', 'apple', '1s9c6', 'dog', 'cs1962', 'sc961'], 'cs196'
#   Output:
#   3
#
# Example 2:
#   Input: ['aabbcc', 'abcabc', 'abcdef', 'defghi'], 'golf'
#   Output:
#   0
#
# Parameters
# ----------
# arr : List[str]
#   A list of strings
#
# uniq : str
#   The string to find anagrams of
#
# Returns
# -------
# int
#   The number of strings in arr that are exact anagrams of uniq.
#
def char_dict_mapping():
    """
    makes a dictioary with all alphabets and numbers mapped to a unique prime number
    """
    #list containing first 36 prime numbers
    prime=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,103, 107, 109, 113, 127,131,137,139,149,151]
    #list containg all chars 0-9 and a-z
    chars=['0','1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    char_mapping={}
    i=0
    for c in chars:
        char_mapping[c]=prime[i]
        i+=1
    return char_mapping
def count_anagrams(arr, uniq):
    """
    Given a list of strings, find the anagrams of uniq in the list and return the count.
    """
    uniq=uniq.lower()
    char_mapping=char_dict_mapping()
    original_product=1
    count=0
    for c in uniq:
        original_product*=char_mapping[c]#unique product of unique prime numbers
    for word in arr:
        word=word.lower()
        product_check=1
        for c in word:
            product_check*=char_mapping[c]
        if product_check==original_product:
            count+=1
    return count