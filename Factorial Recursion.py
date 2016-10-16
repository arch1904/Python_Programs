def fact(n,x):
    x*=n
    if n-1!=0:
        n-=1
        fact(n,x)
        if n==1:
            print(x)
n=int(input("Enter Number For Which Factorial Is To Be Calculated "))
fact(n,1)

    
