print("Enter Elements For First Matrix ")
m1=[]
m2=[]
m=[]
l=[]
for i in range (0,3):
    l=[]
    for j in range(0,3):
        a=int(input("Enter Element "))
        l.append(a)
    m1.append(l)

print("Enter Elements For Second Matrix ")
for i in range (0,3):
    l=[]
    for j in range(0,3):
        a=int(input("Enter Element "))
        l.append(a)
    m2.append(l)
for i in range(0,3):
    l=[]
    for j in range(0,3):
        a=m1[i][j]+m2[i][j]
        l.append(a)
    m.append(l)
for i in range(0,3):
    for j in range(0,3):
        print(m1[i][j]," ",end="")
    print("")
print("\n")
for i in range(0,3):
    for j in range(0,3):
        print(m2[i][j]," ",end="")
    print("")
print("\n")
for i in range(0,3):
    for j in range(0,3):
        print(m[i][j]," ",end="")
    print("")
print("\n")



    
