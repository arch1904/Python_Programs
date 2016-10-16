# Three Sum
#
# Given an array S of n integers and constant 'target', are there elements a, b, c in S such that
# a+b+c = target? Find all unique triplets in the array which gives the sum of target.
# return a 2d list, where all inner lists are triplets. There may be more than
# one pair of triplets.
#
# Runtime: o(n^2) will get full credit.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: [-1, 0, 1, 2, -1, -4], 0
#
#   Output:
#   [
#  [-1, 0, 1],
#  [-1, -1, 2]
#   ]
#
#
# Parameters
# ----------
# arr: array
#   array of numbers
#
# target: int
#   target integer
#
# Returns
# -------
# 2d array
#    2d list, inner lists are triplets that add up to target.
def three_sum(arr, target):
    arr.sort()
    result=[]
    for i in xrange(0,len(arr)-2):
        arr1=arr[i]
        first=i+1
        last=len(arr)-1
        while first<last:
            arr2=arr[first]
            arr3=arr[last]
            if(arr1+arr2+arr3) == target:
                if [arr1,arr2,arr3] not in result:
                    result.append([arr1,arr2,arr3])
                last-=1
            elif (arr1+arr2+arr3)>target:
                last-=1
            else:
                first+=1
    if len(result)>0:
        return result
    return None