# Reverse Block
#
# Given a list/array and a number n, reverse the list in blocks of n.
#
# Let's say the list is [1, 2, 3, 4, 5, 6, 7] and we are given the number 3.
# That must mean that the list must be reversed in groups of 3.
# [3, 2, 1, 6, 5, 4, 7]
#
# Restriction(s)
# --------------
# Block_size will always be a positive integer.
#
# Example(s)
# ----------
# Example 1:
#   Input 1: [1, 2, 3, 4, 5, 6, 7]
#   Input 2: 3
#   We take the list and reverse the elements in groups of 3.
#   Output:
#   [3, 2, 1, 6, 5, 4, 7]
#
# Parameters
# ----------
# arr: list
#   The list/array that must be reversed
# block_size: int
#   The size of each group that we will reverse.
#
# Returns
# -------
# list
#   A list with groups of `block_size` reversed.
def reverse_block(arr, block_size):
    arr1=[]
    i=0
    while i<len(arr):
        arr1.append(arr[i:i+block_size])
        i=i+block_size
    arr=[]
    for i in range(len(arr1)):
        arr1[i]=arr1[i][::-1]
        arr=arr+arr1[i]
    return arr