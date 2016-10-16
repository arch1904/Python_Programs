def func(num,string):
    i=0
    b=""
    while i<len(string):
        if string[i].isdigit():
            b=b+string[i]
        i+=1
    print(num," + ",b," = ",num+int(b))
a=int(input("Enter Number "))
b=input("Enter String ")
func(a,b)

            
            
            
