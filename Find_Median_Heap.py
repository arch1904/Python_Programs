# Find Median
#
# Given a stream of integers, find the new median after every iteration.
# You are given a class that emulates a stream. The insertDataFindMedian method
# represents a single output of the stream into your data structure. After every call
# of this method, return the new median. In other words, you should be modifying the
# functionality of the insertDataFindMedian method. To test, instantiate an object of
# the median class and call the insertDataFindMedian method multiple times.
#
#
# Example(s)
# ----------
# See class notes on heaps!
#
# Parameters
# ----------
# newNumber : double
#
# Returns
# -------
# median : double
#   new median
import heapq
class median(object):
    def __init__(self):
        self.min_heap = []
        self.max_heap = []


    def insertDataFindMedian(self,newNumber):

        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)
        if(len(self.min_heap)==0):
            self.min_heap.append(newNumber)
            heapq.heapify(self.min_heap)
        elif(len(self.max_heap)==0):
            self.max_heap.append(newNumber)
            heapq._heapify_max(self.max_heap)
        elif(newNumber<self.max_heap[0]):
            self.max_heap.append(newNumber)
            heapq._heapify_max(self.max_heap)
        else:
            self.min_heap.append(newNumber)
            heapq.heapify(self.min_heap)
        if(len(self.max_heap)==len(self.min_heap)):
        	pass
        if(len(self.max_heap)-len(self.min_heap)>1):
            while len(self.max_heap)-len(self.min_heap)>1:
                n=heapq.heappop(self.max_heap)
                self.min_heap.append(n)
            heapq.heapify(self.min_heap)
        elif (len(self.min_heap)-len(self.max_heap)>1):
            while len(self.min_heap)-len(self.max_heap)>1:
                n=heapq.heappop(self.min_heap)
                self.max_heap.append(n)
            heapq._heapify_max(self.max_heap)
        if(len(self.max_heap)==len(self.min_heap)):
        	median=((float(self.max_heap[0]))+self.min_heap[0])/2
        else:
        	if(len(self.max_heap)>len(self.min_heap)):
        		median = self.max_heap[0]
        	else:
        		median= self.min_heap[0]
    	return median
