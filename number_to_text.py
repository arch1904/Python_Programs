# Number to Text
#
# Write a function that given a number from 0-100, will return the string which is a English representation of the number.
# The result should be lower case and spaced out with no dashes
#
# Your solution should run in O(n) time. Your solution should not allocate
# any space other than the output list.
#
# Example(s)
# ----------
# Example 1:
#   Input: 100
#   Output: one hundred
#
# Example 2:
#   Input: 74
#   Output:
#   seventy four
#
# Example 3:
#   Input: 19
#   Output:
#   nineteen
#
# Example 4:
#   Input: 28
#   Output:
#   twenty eight
#
# Parameters
# ----------
# number : int
#   A number from 0-100
#
# Returns
# -------
# string
#   English representation of the number
#

def basic_check(n):
    #Function To Assign Every Digit or some basic numbers to their corresponding strings
    if n==0:
        return "zero"
    elif n==1:
        return "one"
    elif n==2:
        return "two"
    elif n==3:
        return "three"
    elif n==4:
        return "four"
    elif n==5:
        return "five"
    elif n==6:
        return "six"
    elif n==7:
        return "seven"
    elif n==8:
        return "eight"
    elif n==9:
        return "nine"
    elif n==11:
        return "eleven"
    elif n==12:
        return "twelve"
    elif n==13:
        return "thirteen"
    elif n==14:
        return "fourteen"
    elif n==15:
        return "fifteen"
    elif n==16:
        return "sixteen"
    elif n==17:
        return "seventeen"
    elif n==18:
        return "eighteen"
    elif n==19:
        return "nineteen"
    elif n==10:
        return "ten"
    elif n==20:
        return "twenty"
    elif n==30:
        return "thirty"
    elif n==40:
        return "fourty"
    elif n==50:
        return "fifty"
    elif n==60:
        return "sixty"
    elif n==70:
        return "seventy"
    elif n==80:
        return "eighty"
    elif n==90:
        return"ninety"
    elif n==100:
        return"hundred"
    else:
        return None
def number_to_text(number):
    if basic_check(number) is not None:
        return basic_check(number)
    elif number>=0 and number<=100:
        return basic_check(number-number%10) + ' ' + basic_check(number%10)
    else:
        return "OUT OF BOUNDS!"
