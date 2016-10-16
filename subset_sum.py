# Subset Sum
#
# Given a list of unsorted integers and another integer k, determine if you can
# sum an arbitrary number of elements of the list and get exactly k.
#
# Note: You can use each element in the list exactly once while calculating the
#       sum.
#
# Example(s)
# ----------
# Example 1:
#   Input: [1,5,4,3,6,2,5,17], 24
#   17 + 4 + 2 + 1 = 24
#   Output:
#   True
#
# Example 2:
#   Input: [1,18,5], 10
#   No elements will sum to 10
#   Output:
#   False
#
# Parameters
# ----------
# arr : List[int]
#   An unsorted list of integers
#
# k : int
#   The integer you are trying to sum to
#
# Returns
# -------
# bool
#   Whether or not k can be constructed from a subset sum of arr
#
from itertools import combinations
def subset_sum(arr, k):
    a=list()
    for i in range(1,len(arr)+1):
        a=list(combinations(arr,i))
        for j in range(0,len(a)):
            if sum(a[j])==k:
                return True
            else:
                continue
    return False