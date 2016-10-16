f=open("file.txt",'r')
str=' '
m=list()
while str:
    str=None
    str=f.readline()
    m=str.split('~')
    print(m)
    print(m[0]," Average Marks ",((int(m[1])+int(m[2])+int(m[3])+int(m[4])+int(m[5]))/5))
f.close()
    
