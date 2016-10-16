###############################################################################
# Caesar Cipher
#
# Caesar Cipher is an old way to encrypt secret messages across two users,
# by using a number to each word in the sentence by.
#
# We will be using the alphabet A-Z, a-z, then 0-9, which means the alphabet you will be shifting
# through will contain 62 characters.
#
# For reference here is the alphabet you will be shifting through:
#
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# a b c d e f g h i j k l m n o p q r s t u v w x y z
# 0 1 2 3 4 5 6 7 8 9
#
# where A is the first character in the alphabet, B is the second, C is the third, and so on.
# Please ignore any characters not in the alphabet, and keep them the same as before.
#
# Given a string and the number of shifts, RETURN the resulting string of the caesar cipher operation.
#
# Example(s)
# ----------
# Example 1:
#   Input: caesar_cipher('Test.', 15)
#   You will need to encode the string 'Test.', by shifting right by 15.
#   T + 15 = i
#   e + 15 = t
#   s + 15 = 7
#   t + 15 = 8
#   . -> . (Keep everything not in the alphabet out)
#   Output:
#   'it78.'
#
# Parameters
# ----------
# sentence : String
#   The sentence that must be encoded.
# shifts : Int
#   The number of right shifts that should be done on the string.
#
# Returns
# -------
# String
#   The Caesar Cipher of the sentence shifted right by shift.
#
def caesar_cipher(sentence, shifts):
    """
    Given a sentence and the number of shifts, RETURN the resulting caesar cipher.

    >>> caesar_cipher('Test.', 15)
    'it78.'
    >>> caesar_cipher('Encoded strings are difficult to read', 30)
    'iH6I787 MNLCHAM 4L8 7C99C6OFN NI L847'
    >>> caesar_cipher('3Q JZf xLY CPLO ESTd AWPLdP DPYO 2PWa!', 15)
    'If You Can Read This Please Send Help!'
    """
    # Your code goes here!
    base=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
    temp=""
    for c in sentence:
        if c in base:
            a=""
            i=0
            while c!=a and i<len(base) :
                a=base[i]
                i=i+1
            i=i-1
            i=i+shifts
            if i>61:
                i=i-62
            temp=temp+base[i]
        else:
            temp=temp+c
    sentence=""
    sentence=sentence+temp
    return sentence       