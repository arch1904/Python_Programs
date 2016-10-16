#Runs In Python 3
for i in range (0,5,1):
    for s in range(5,i,-1):
        print(" ",end="")
    
    print("*",end="")
    for t in range(0,i,1):
        print("  ",end="")
    if i>0:
        print("*",end="")
    print("")

for i in range (0,12,1):
    print("*",end="")
