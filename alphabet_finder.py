# Alphabet Finder
#
# Given a string, find the shortest prefix where all letters of the alphabet first appears.
# If there is no prefix such that all the letters of the alphabet appear, return None.
#
# Example(s)
# ----------
# Example 1:
#   Input: 'abcdefghijklmnopqrstuvwxyz'
#   This is just the alphabet.
#   Output:
#   'abcdefghijklmnopqrstuvwxyz'
#
# Example 2:
#   Input: 'hi!abcdefghijklmnopqrstuvwxy you wont see a z till there!'
#   The alphabet first appears where the first z appears.
#   Output:
#   'hi!abcdefghijklmnopqrstuvwxy you wont see a z'
#
# Example 3:
#   Input: 'Wait, what if a sentence does not have all letters?'
#   There is no alphabet in the input.
#   Output:
#   None
#
# Parameters
# ----------
# arg1 : String
#   Input String
#
# Returns
# -------
# str
#   The prefix that the alphabet first appears.
# None
#   There is no complete alphabet.
#
def alphabet_finder(sentence):
    """
    Given a string, find the shortest prefix where all the letters of the alphabet first
    appears.
    """
    sentence1=sentence.lower()
    #Dictionary with all alphabets as keys and mapped to 1
    contains={'a':1, 'b':1, 'c':1, 'd':1, 'e':1, 'f':1, 'g':1, 'h':1, 'i':1, 'j':1, 'k':1, 'l':1, 'm':1, 'n':1, 'o':1, 'p':1, 'q':1, 'r':1, 's':1, 't':1, 'u':1, 'v':1, 'w':1, 'x':1, 'y':1, 'z':1}
    last_index=0
    #boolean to check when all alphabets have been found in a sentence
    check=False
    for i in range(0,len(sentence1)):
        if sentence1[i].isalpha() and contains[sentence1[i]] == 1:
            contains[sentence1[i]] = 0
        for key in contains: #To Check If All Alphabets have been found in the sentence
            if contains[key]!=0:
                check=False
            else:
                check=True
        if check:
            last_index=i #Index where all alphabets have been found in the sentence
            break
    if check:
        return sentence[0:last_index+1]
    else:
        return None