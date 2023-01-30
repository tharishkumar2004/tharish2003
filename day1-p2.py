z=[]
x=int(input("enter the integer"))
for i in range(x):
    n=int(input("enter the number"))
    z.append(n)
even=0
odd=0
l=[]
for i in z:
    if(i%2==0):
        even=even+i**2
    else:
        odd=odd+i**2
l.append(odd)
l.append(even)
print(l)
