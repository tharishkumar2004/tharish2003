a=[]
n=int(input("enter number of elements:"))
for i in range(1,n+1):
    b=int(input("enter elements:"))
    a.append(b)
k=0
num=int(input("enter the number to be counted:"))
for j in a:
    if(j==num):
        k=k+1
print("number of times",num,"appear is",k)
