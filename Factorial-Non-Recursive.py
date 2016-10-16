def factorial(n):
    x=1
    for i in range (n,0,-1):
        x*=i
    print(n,"! = ",x)
n=int(input("Input Number To Calculate Factorial"))
factorial(n)
