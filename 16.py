a=[]
n=int(input("enter the number of element in list:")) #5
for i in range(n): # 0,1,2,3,4
    element=input("enter the element "+str(i+1)+":") #0
    a.append(element)
a[0],a[n-1]=a[n-1],a[0]
print("new list is:")
print(a)


