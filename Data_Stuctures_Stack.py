stack=[]
top= -1
def push():

    global top
    n=int(input("Enter Element "))
    stack.append(n)
    top=top+1
def Pop():
    global top
    
    a=stack.pop()
    print(a," is deleted")
    top=top-1
def underflow():
    if top==-1:
        print("UNDERFLOW")
        return 1
    else:
        return 0
def display():
    print(stack)
c='y'
i=0
while c=='y':
    print("To PUSH Enter 1 ")
    print("To POP Enter 2 ")
    print("To Display Enter 3 ")
    print("To Exit Enter 4 ")
    i=int(input())
    print(i)
    1
    if i==1:
        push()
    elif i==2:
        if underflow()==1:
            print("UNDERFLOW")
        else:
            Pop()
    elif i==3:
        display()
    elif i==4:
        c='n'
    c=input("Do You Want To Continue y/n? ")
    
    
    
