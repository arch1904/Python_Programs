# Zero Sum
#
# Return True if a subarray (not any element) summed can create 0.
# Otherwise return False.
#
# Restrictions
# ------------
# Your runtime must be O(n). You can assume the running time of updating a dictionary is O(s)
# where s is the size of the smaller dictionary (constant if you update a dictionary with finite
# elements).
#
# You CANNOT assume the order given will be sorted.
#
# Example(s)
# ----------
# Example 1:
#   Input: zero_sum([0, 1, 2, 3, 4, 5])
#   We need to see if a subarray can create 0.
#   The first element gives us 0. So there is a subarray that can create 0.
#   Output:
#   True
#
# Example 2:
#   Input: zero_sum([10, 20, -20, 3, 21, 2, -6])
#   We need to see if a subarray can create 0.
#   The subarray [20, -20] can create zero.
#   Output:
#   True
#
# Parameters
# ----------
# arr : list
#   A list/array of integers.
#
# Returns
# -------
# Bool
#   True if a subarray can be 0.
#   False if a subarray cannot be 0.
#
def zero_sum(arr):
    """
    Returns if the given list has a subarray that sums to 0.
    """
    dict_sums = {} #empty dictionary
    sum = 0
    if 0 in arr: #if 0 in array then definitely a subarray will sum to 0
        return True
    for i in xrange(len(arr)):
        sum += arr[i] #gets sum of elements until now
        # if any sum reappears then an equal addition and subtraction has been made
        #therefore a subarray can sum to 0
        if sum in dict_sums:
            return True
        else:
            dict_sums[sum] = i
    return False
#