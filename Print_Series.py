from math import *
n=int(input("Enter N "))
x=int(input("Enter X "))
sum=1
flag=0
y=1
for i in range(1,n+1,1):
    term=(pow(x,i))/(factorial(y))
    y=y+2
    if flag%2==0:
        sum-=term
    else:
        sum+=term
    flag+=1
print("Sum Is ",sum)
