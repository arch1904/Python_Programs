# Advanced Divide
#
# Given 2 numbers, divide the first with the second.
# However, you must return an integer when the number is an integer,
# otherwise return a float.
#
# Restrictions
# ------------
# Zero will not be given as one of the arguments
#
# Example(s)
# ----------
# Example 1:
#   Input: advanced_divide(5, 6)
#   We want to divide 5 by 6. The result is a fraction, so we need to represent it as a float
#
#   Output:
#   0.8333333333333334
#
# Example 2:
#   Input: advanced_divide(10, 5)
#   We want to divide 10 by 5. The result is an integer, so we need to represent it as an integer.
#
#   Output:
#   2
#
# Parameters
# ----------
# num1 : int or float
#   The number that will get divided.
# num2 : int or float
#   The number that will divide.
#
# Returns
# -------
# int or float
#   An integer if the division should produce an integer.
#   A float if the division is a fraction.
def advanced_division(num1, num2):
    if num1%num2!=0:
        return(float(num1)/float(num2))
    elif num1%num2==0:
        return(int(num1/num2))