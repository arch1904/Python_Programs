###############################################################################
# Remove Given String
#
# You will be given a string and a removal string, and you will
# need to remove the removal string (both upper and lower case)
# from the string and then return your result.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: ("." , "Hello. I'm Frodo.")
#   You should remove all periods.
#   Output:
#   "Hello I'm Frodo"
#
# Parameters
# ----------
# remove_str : str
#   String to remove
# word : str
#   Word to remove character from
#
# Returns
# -------
# str
#   The string you removed the character from
#
def remove_given_str(remove_str, word):
    """
    Removes remove_str from word

    >>> print remove_given_str("H","Harry is hot in Hogwarts")
    arry is ot in ogwarts
    >>> print remove_given_str("oops","Whoopsie, I made an oopsie. Oops!")
    Whie, I made an ie. !
    """
    # Your code goes here!
    temp=""
    word1=word.lower()
    remove_str=remove_str.lower()
    index=[]
    for i in range(0,len(word1)):
        if word1[i:i+len(remove_str)]==remove_str:
            for j in range(i,i+len(remove_str)):
                index.append(j)
    for i in range(0,len(word)):
        if i in index:
            pass
        else:
            temp=temp+word[i]
    word=''
    word=word+temp
    return(word)