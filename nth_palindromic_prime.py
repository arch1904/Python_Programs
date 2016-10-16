# nthPalindromicPrime
#
# Given a non-negative integer n return the nth palindromic prime
# A palindromic prime is a number that is both prime and a palidrome - a prime number that is read the same backwards and forwards.
# Some examples of palindromic primes: 2,3,5,7,11,101,131,151,181,191,313
# For example, if n = 3, the third palindromic prime is 5. Return 5.
#
# Example(s)
# ----------
# Example 1:
#   Input: 5
#   What is the 5th palindromic prime? It is 11
#   Output:
#   11
#
# Example 2:
#   Input: 8
#   What is the 8th palindromic prime? It is 151
#   Output:
#   151
#
# Parameters
# ----------
# n : a non-negative integer
#
# Returns
# -------
# bool
#   the nth palindromic prime
#
# hint: write a helper function isPalindromicPrime(n) first!
def isPalindromicPrime(num1):
    if palindrome(num1) and prime_test(num1):
        return True
    else:
        return False

def nthPalindromicPrime(n):
    count=0
    i=0
    pp=0
    while count!=n:
        if isPalindromicPrime(i):
            count+=1
            pp=i
        else:
            pass
        i+=1
    return pp