a=[]
n=int(input("enter the  number of element in list:"))
for x in range(n):
    element=int(input("enter the number elements in list:"))
    a.append(element)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print("new list is:")
print(a)
