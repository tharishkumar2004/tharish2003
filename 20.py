#find the largest number present in the list
a=[]
n=int(input("enter the number of element:"))
for i in range(1,n+1):
    b=int(input("enter the element:"))
    a.append(b)
a.sort()
print("largest element is:",a[n-1])
