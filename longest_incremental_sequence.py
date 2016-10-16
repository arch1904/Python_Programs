# Longest Incremental Sequence
#
# Given a list, find the longest sequence in the list.
# The sequence we want to find is defined to be the sequence in which
# the number be a certain number is one less.
# For example: [1, 2, 3, 4] would be a sequence we want to find, as well as,
# [5, 6, 7, 8] or [10, 11, 12] OR [101, 102, 103]. However, we do not want a sequence like
# [10, 20, 30, 40...] or [55, 60, 65, 70, 75...].
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
#   Input: [9, 3, 4, 1, 2, 100, 200, 1, 4]
#   Here, the longest sequence will be [1, 2, 3, 4]. Note a couple of things:
#   The order of appearance did not matter.
#   The sequence is defined to be incremented by 1. So we won't be looking for something like
#   [100, 200, 300] etc. Only a subsequence in order. i.e. [1, 2, 3, 4] or [5, 6, 7, 8].
#
#   Output:
#   4
#
# Example 2:
#   Input: [10, 20, 30, 40, -1, -2, -3, 0, 1, 2, 3, 100]
#   It is a bit easier to see than example 1. Nonetheless, the same principles apply.
#   The longest sequence here would be [-3, -2, -1, 0, 1, 2, 3].
#
#   Output:
#   7
#
# Parameters
# ----------
# arr : list
#   A list/array of integers.
#
# Returns
# -------
# int
#   The number of elements the longest incremental sequence the list has.
#
def longest_incremental_sequence(arr):
    """
    Given a list, returns the longest incremental sequence.
    """
    arr_sorted=sorted(arr) #sorts array and stores in new array
    count =1
    max_sequence=0
    for i in range(1,len(arr_sorted)):
        #if next element is consecutive increase count by 1
        if arr_sorted[i-1]+1 == arr_sorted[i]:
            count+=1
        else:
            #if series breaks reset count to 1
            count = 1
        # look for largest sequence
        if max_sequence<count:
            max_sequence=count
    return max_sequence