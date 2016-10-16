a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if a>b>c:
    print(c,b,a)
elif b>a>c:
    print(c,a,b)
elif a>c>b:
    print(b,c,a)
elif b>c>a:
    print(a,c,b)
elif c>b>a:
    print(a,b,c)
elif c>a>b:
    print(b,a,c)
