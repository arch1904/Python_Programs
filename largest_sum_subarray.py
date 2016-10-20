# Largest Sum Subarray
#
# Write a function that given an array of integers will return the continuous subarrray with the largest
# sum in the entire array
#
#
# Example(s)
# ----------
# Example 1:
#   Input: [-8,-6,1,-4,3,4,6]
#   Output: [3,4,6]
#
# Example 2:
#   Input: [2,-8,7,-3,4,-20]
#   Output: [7,-3,4]
#
# Example 3:
#   Input: [-1,-2,-3,-4]
#   Output: [-1]
#
# Parameters
# ----------
# arr : List[int]
#   A variable length array of integers
#
# Returns
# -------
# List[int]
#   Largest sum continous sub array
#
def largest_sum_subarray(arr):
    '''
    returns the largest sum continous sub array
    '''
    if len(arr) == 0: #If Arr is Empty Return None
       return None
    sum = max_sum = arr[0] #initialising sum and max sum to first element of the array
    i = 0
    first = last = 0
    for j in range(1, len(arr)): #Iterate through list starting at the second element
        if arr[j] > (sum + arr[j]): #if current element is greater than sum + current element
            sum = arr[j]
            i = j
        else:
            sum += arr[j] #keep adding consecutive elements

        if sum > max_sum: 
            max_sum = sum #get maximum sum
            first = i #index where largest sum subarray starts
            last = j #index where largest sum subarray ends
    return arr[first:last+1]