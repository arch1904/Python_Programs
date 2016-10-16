# Happy Numbers
#
# A happy number is a positive integer with the following characteristic: if we
# take ths sum of the square of its digits to get another number, and take the
# sum of the squares of that number and continue this process, we eventually
# get the number 1. If a number is not happy, we will get stuck in a cycle that
# does not include the number 1.
#
# Your task is to find the number of happy numbers between 0 and the given
# integer n.
#
# Calculation Example:
# 19 is a happy number.
# 19 -> 1^2 + 9^2 = 1 + 81 = 82
# 82 -> 8^2 + 2^2 = 64 + 4 = 68
# 68 -> 6^2 + 8^2 = 36 + 64 = 100
# 100 -> 1^2 + 0^2 + 0^2 = 1.
#
# Example(s)
# ----------
# Example 1:
#   Input: 8
#   Between 0 and 8, numbers 1 and 7 are happy numbers
#   Output:
#   2
#
# Example 2:
#   Input: 15
#   Between 0 and 25, numbers 1, 7, 10, and 13 are happy numbers
#   Output:
#   4
#
# Parameters
# ----------
# n : int
#   The high end of the range you need to check for happy numbers
#
# Returns
# -------
# int
#   The number of happy numbers between 0 and n (exclusive)
#
square_dictionary=dict([(c,int(c)**2) for c in "0123456789"])
def is_happy(num):
    l = [] #list to hold values already checked for
    sum1=0 #holds sum each time
    while sum1!=1 and num not in l :
        l.append(num)
        sum1=0
        num=list(str(num))
        for i in num:
            sum1=sum1+square_dictionary[i]
        if sum1==1:
            return True
        else:
            num=sum1 #assigns num to the sum if sum!=1
    return False

def happy_numbers(n):
    """
    Given an integer input, return the number of happy numbers between 0 and n
    """
    no_happy_nos=0
    for i in range(0,n):#iterates from 0 to input n to check if each no is happy
        if is_happy(i):
            no_happy_nos+=1
        else:
            continue
    return no_happy_nos