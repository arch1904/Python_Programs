a=input("Enter String ")
b=""
for i in range(0,len(a)):
    if i==0:
        b=b+a[i]+"."
    elif a[i-1]==" ":
        b=b+a[i]+"."
print(b)
