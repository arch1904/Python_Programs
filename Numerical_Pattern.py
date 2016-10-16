#Runs In Python 3
for i in range (0,5,1):
    for s in range(4,i-1,-1):
        print(" ",end="")
    for j in range(1,i+2,1):
        print(j,end="")
    
    if i>0:
        for k in range(i,0,-1):
            print(k,end="")
    print("")

for i in range(4,-1,-1):
    for s in range(i,6,1):
        print(" ",end="")
    for j in range(1,i+1,1):
        print(j,end="")
    if i>0:
        for k in range(i-1,0,-1):
            print(k,end="")
    print("")
    
