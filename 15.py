#sum of the list with recursion
def sum_arr(arr,size):
    if(size==0):
        return 0
    else:
        return arr[size-1]+sum_arr(arr,size-1)
n=int(input("enter the number of element for list:"))
a=[]
for i in range(n):
    element=int(input("enter the number:"))
    a.append(element)
print("the listis:")
print(a)
print("sum of items in list:")
b=sum_arr(a,n)
print(b)
