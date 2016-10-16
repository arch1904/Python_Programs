a=input("Enter String ")
i=0
lower=0
upper=0
num=0
specialchar=0
while i<len(a):
    if ord("A")<=ord(a[i]) and ord(a[i])<=ord("Z"):
        upper+=1
    elif ord("a")<=ord(a[i]) and ord(a[i])<=ord("z"):
        lower+=1
    elif ord("1")<=ord(a[i]) and ord(a[i])<=ord("9"):
             num+=1
    else:
             specialchar+=1
    i+=1
print("No Of Lower Case = ",lower)
print("No Of Upper Case = ",upper)
print("No Of Numeric Characters = ",num)
print("No Of Special Characters = ",specialchar)

