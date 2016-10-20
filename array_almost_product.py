# Array Almost Product
#
# Write a function that, given a list of integers, will return a list of
# integers 'output' wherein the value of output[i] is the product of all the
# numbers in the input array except for input[i].
#
# Note: Your solution *cannot* use division in any way.
#
# Your solution should run in O(n) time. Your solution should not allocate
# any space other than the output list.
#
# Example(s)
# ----------
# Example 1:
#   Input: [2,3,4,5]
#       Output should be [3*4*5, 2*4*5, 2*3*4]
#   Output: [60, 40, 30, 24]
#
# Example 2:
#   Input: [3,6,9,-3,2,-2]
#   Output:
#   [648, 324, 216, -648, 972, -972]
#
# Parameters
# ----------
# arr : List[int]
#   A list of integers. You can assume len(arr) > 1
#
# Returns
# -------
# List[int]
#   Returns a list where every element of the list is the product of
#   all the numbers in the input list except for the number at the index
#   being evaluated.
#
def array_almost_product(arr):
    '''
    returns a list with product all numbers in the input list except for the number at the index being evaluated
    '''
    output=[1]*len(arr)#initialise list with 1
    p=1
    for i in range(0,len(arr)):
        output[i]=p #current element = product of elements before it
        p*=arr[i] #update p by multiplying with current value
    p=1
    for i in range(len(arr)-1,-1,-1): #go backwards
        output[i]*=p #multiplying every element with value of p
        p*=arr[i] #update p by multiplying with current value
    return output