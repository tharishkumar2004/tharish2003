a=[]
n=int(input("enter the number of elementin list:"))
for x in range(0,n):
    element=int(input("enter the element"+str(x+1)))
    a.append(element)
b=set()
unique=[]
for x in a:
    if x not in b:
                unique.append(x)
                b.add(x);
print("non duplicate items:")
print(unique)
