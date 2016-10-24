'''
Largest Rectangular Area Under Histogram
Find the largest rectangular area possible in a given histogram where the largest rectangular area can be formed by contigous bars.
Assume widths are 1 unit of each bar.
Runtime : O(n)
Input: [6,2,5,4,5,2,6]
Output: Int Area (3*4) in this case (area b'w 5-4-5)
'''
def calc_area(arr):
	area=min(arr)*len(arr)
	return area

def sub_lists(arr):
	lists=[]
	length = len(arr)
	for i in range(1, length + 1):
		for start in range(0, (length - i) + 1):
			lists.append(arr[start:i+start])
	return lists

def largest_rectangular_area(histogram):
	lists=sub_lists(histogram)
	max_area=0
	max_list=[]
	for i in range(0,len(lists)):
		area=calc_area(lists[i])
		if area>max_area:
			max_list=lists[i]
			max_area=area
	return max_area

print largest_rectangular_area([6,2,5,4,5,1,6])
