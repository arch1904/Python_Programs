a=int(input("Enter a "))
b=int(input("Enter b "))
c=int(input("Enter c "))
x1=-b+pow(b*b-4*a*c,(1/2))
x2=-b-pow(b*b-4*a*c,(1/2))
if b*b-4*a*c>0 :
    print("real roots")
elif b*b-4*a*c<0 :
    print("imaginary roots")
if x1==x2:
    print("Equal Roots")
    
