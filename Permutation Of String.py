string=input("Enter A String ")
for i in range (0,len(string)):
    
    for j in range(0,len(string)):
        b=""
        k=0
        if i==j:
            continue
        else:
            while k<len(string):
                if k!=i and k!=j:
                        b=b+string[k]
                elif k==i:
                    b=b+string[j]
                elif k==j:
                    b=b+string[i]
                k=k+1
        
            print(b)
                    
            
            
        
