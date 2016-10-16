from math import *
def calc():
    print("To Calulate Sum Enter +")
    print("To Calculate Difference Enter -")
    print("To Calculate Product Enter *")
    print("To Calculate Quotient Enter /")
    c=input("Enter Choice")
    n=0
    while(n==0):
        if c not in('+','-','*','/'):
            print("Invalid Option, Enter Valid Choice")
            n=0
        else:
            n=1
    return c
def sum():
    a=int(input("Enter First Value"))
    b=int(input("Enter Second Value"))
    c=a+b
    print("Sum is ",c)
def difference():
     a=int(input("Enter First Value"))
     b=int(input("Enter Second Value"))
     c=a-b
     print("Difference is ",c)
def product():
         a=int(input("Enter First Value"))
         b=int(input("Enter Second Value"))
         c=a*b
         print("Product is ",c)
def quotient():
          a=int(input("Enter First Value"))
          b=int(input("Enter Second Value"))
          c=a/b
          print("Difference is ",c)
c=calc()
if c=='+':
    sum()
elif c=='-':
    difference()
elif c=='*':
    product()
elif c=='/':
    quotient()
    
        
        
