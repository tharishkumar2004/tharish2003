#spliting the list
a=[]
n=int(input("enter the number of element:"))
for i in range (1,n+1):
    b=int(input("enter the number:"))
    a.append(b)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("the even list",even)
print("the odd list",odd)
