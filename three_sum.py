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
    '''
    returns a 2d list where the inner lists are triplets that add up to the target
    '''
    arr.sort() #sort the array first
    result=[] #empty list to hold the resulting arrays
    for i in xrange(0,len(arr)-2):
        arr1=arr[i] #first element
        first=i+1 #starting
        last=len(arr)-1 #end
        while first<last: 
            arr2=arr[first] #second element
            arr3=arr[last] #Third Element
            if(arr1+arr2+arr3) == target: #do the first, second and third elements sum to the targer
                if [arr1,arr2,arr3] not in result: #is this combination already in the result list?
                    result.append([arr1,arr2,arr3])
                last-=1 #decrease last
            elif (arr1+arr2+arr3)>target: # if the sum is greater decrease third element
                last-=1
            else:
                first+=1 #if the sum is less increase second element
    if len(result)>0:
        return result[::-1]
    return None
