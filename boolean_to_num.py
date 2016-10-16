###############################################################################
# To Integer
#
# Take a list of booleans and return an integer made from its binary
#
#
# Example(s)
# ----------
# Example 1:
#   Input: "true,false,true,false"
#   The decimal equivalent of 1010 is 10
#   Output:
#   10
#
# Parameters
# ----------
# arr : str
#   Comma separated string list of booleans
#
# Returns
# -------
# int
#   Int representation of the sum of strings from the list
#
def to_int(arr):
    """
    Converts a list of booleans into an integer

    >>> print to_int("true,false,true,true")
    11
    >>> print to_int("true,false,false,false,true")
    17
    """
    # Your code goes here!
    arr=arr.split(",")
    bin1=""
    for c in arr:
        if c=="true":
            bin1=bin1+"1"
        elif c=="false":
            bin1=bin1+"0"
        else:
            print("WRONG INPUT!!!")
            exit()
    p=len(bin1)-1
    num=0
    for c in bin1:
        if c=="1":
            num=num+pow(2,p)
        p=p-1
    return(num)