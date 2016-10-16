

def prime(n):
    count=0
    for i in range (2,n,1):
        x=n%i
        if x==0:
            count+=1
    if count>0:
        print("It Is Not A Prime Number")
    elif count==0:
        printf("It Is A Prime Number")
n=int(input("Input Number To Check Prime"))
prime(n)

    
