queue=[]
front,rear=-1,-1
def insert():
    global front,rear
    if front==-1:
        front+=1
    rear+=1
    n=int(input("Enter Value "))
    queue.append(n)
def dele():
    global front,rear
    if rear==-1:
        print("UNDERFLOW")
    elif front==rear:
        front-=1
        rear-=1
    else:
        del queue[front]
        rear-=1
def display():
    print(queue)
c='y'
i=0
while c=='y':
    print("To Insert Enter 1 ")
    print("To Delete Enter 2 ")
    print("To Display Enter 3 ")
    print("To Exit Enter 4 ")
    i=int(input())
    print(i)
    1
    if i==1:
        insert()
    elif i==2:
            dele()
    elif i==3:
        display()
    elif i==4:
        c='n'
    c=input("Do You Want To Continue y/n? ")
    

    
