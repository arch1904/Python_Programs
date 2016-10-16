list=[10,9,8,7,6,5,4,3,2,1]
def selection_sort():
    global list
    for i in range (0,len(list)):
        min=list[i]
        pos=i
        for j in range(i+1,len(list)):
            if min>list[j]:
                min=list[j]
                pos=j
        list[i],list[pos]=list[pos],list[i]
    print(list)
selection_sort()
