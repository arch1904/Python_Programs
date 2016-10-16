###############################################################################
# CSVify
#
# Often, you will need to take some sort of data and condition it to be in a
# particular format. In this case, we will take a long string and manipulate it
# to behave like a comma-separated-value file. To do this, you should remove
# the whitespace between words in the string and RETURN the conditioned string
# whilst keeping intact line breaks.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: 'the quick  brown   fox\njumped    over the  lazy   dog'
#   Should replace all the whitespace between the words with commas
#   Output:
#   'the,quick,brown,fox\njumped,over,the,lazy,dog'
#
# Parameters
# ----------
# raw_str : str
#   A (potentially) multilined string containing words, newlines, and
#   whitespace
#
# Returns
# -------
# str
#   The comma-separated string
#
def csvify(raw_str):
    """
    Removes whitespaces and replaces with commas

    >>> print csvify('the quick  brown   fox\\njumped    over the  lazy   dog')
    the,quick,brown,fox
    jumped,over,the,lazy,dog
    >>> print csvify('subject course   term\\n CS 196    Fall16\\nCS 125     Fall16')
    subject,course,term
    CS,196,Fall16
    CS,125,Fall16
    """
# Your code goes here!
    str1=""
    s=0
    for c in raw_str:
        if c==" ":
            if s==0:
                str1=str1+","
                s=1
            else:
                str1=str1+""
        else:
            str1=str1+c
            s=0
        if "\n" in c:
            s=1
    return str1