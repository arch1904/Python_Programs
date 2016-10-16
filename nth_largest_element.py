# Nth Largest Element
#
# Write a function that, given an unsorted array, returns the nth largest
# element in that array. So, if n is 1, return the largest element, if n is
# 2 return the second-largest element, and so on.
#
# Note: You may not use any built in sorting methods for this problem.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: [3,1,5,2,4], 3
#   Output:
#   3
#
# Example 2:
#   Input: [-331, -776, 917, 399, -768, -183, -116, 278, -544, -669], 5
#   Output:
#   -183
#
# Parameters
# ----------
# arr : List[int]
#   An unsorted list of integers
#
# n : int
#   An integer in range 1 < n < len(arr)
#
# Returns
# -------
# int
#   The nth largest element in arr
#
def bubble(arr):
    length = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr;

def nth_largest_element(arr, n):
    arr=bubble(arr)
    return(arr[n*-1])