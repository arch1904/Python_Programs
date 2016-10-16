# Prime Test
#
# A prime number is any natural number greater than 1 which has no positive
# divisors other than 1 and itself. In this function, you will get an integer
# and RETURN a boolean representing whether or not the number is prime.
#
# (Pat yourself on the back if you're able to prime check 961748941 in under
#  a second)
#
# Example(s)
# ----------
# Example 1:
#   Input: 13
#   13 has no divisors other than 1 and itself
#   Output:
#   True
#
# Example 2:
#   Input: 24
#   24 is divisible by 2, so it is not a prime number
#   Output:
#   False
#
# Parameters
# ----------
# num : int
#   The integer to check for being prime.
#   For the purposes of this problem, num < 10**5
#
# Returns
# -------
# bool
#   Whether or not 'num' is a prime number
#
def prime_test(num):
    flag=0
    for i in range(1,num+1):
        if num%i==0:
            flag+=1
        else:
            pass
    if flag>2 or flag<2:
        return(False)
    elif flag==2:
        return(True)