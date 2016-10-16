# Fibonacci Sequence
#
# Given a number n, print the nth fibonacci sequence.
#
# Restrictions
# ------------
# We will not test a number larger than 10.
#
# Example(s)
# ----------
# Example 1:
#   Input: fibonacci(4)
#   The fourth fibonacci number can be calculated by doing a sequence.
#   1, 1, 2, 3, 5,...
#   The fourth sequence is 3.
#   Output: 3
#
# Example 2:
#   Input: fibonacci(5)
#   The fifth fibonacci number can be calculated by doing a sequence.
#   1, 1, 2, 3, 5,...
#   The fourth sequence is 5.
#   Output: 5
#
# Parameters
# ----------
# num : int
#   Num is the nth number of the sequence you need to calculate.
#
# Returns
# -------
# num : int
#   The nth number in the fibonnaci sequence
def fibonacci(num):
    if num==-1:
        return(1)
    else:
        count=0
        a=0
        b=1
        fib=0
        while count<num-1:
            fib=a+b
            a=b
            b=fib
            count+=1
        return(fib)