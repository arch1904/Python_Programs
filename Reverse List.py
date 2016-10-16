l=[1,2,3,4,5,6,7,8,9,10]
l1=[]
t=l[len(l)-1]
for i in range (len(l)-1,0,-1):
    l[i]=l[i-1]
l[0]=t    
for i in range(0,len(l)):
    print(l[i]," ",end="")
print("")

    
