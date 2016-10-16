list=[10,9,8,7,6,5,4,3,2,1]
def insertionsort():
    global list
    for i in range (1,len(list)):
        temp=list[i]
        j=i-1
        while temp<list[j] and j>=0 :
            list[j+1]=list[j]
            j-=1
        list[j+1]=temp
    print(list)
insertionsort()
