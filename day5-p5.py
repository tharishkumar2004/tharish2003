def shuffle(n,m):
    for j in range (8):
        print(n[j],m[j],n[j+1],m[j+1])
list1=[]
list2=[]
a=int(input("enter the number of elements for list 1:"))
for i in range (1,a+1):
      b=int(input("enter the number:"))
      list1.append(b)
print(list1)
c=int(input("enter the number of elements for list 2:"))
for i in range (1,c+1):
    d=int(input("enter the number :"))
    list2.append(d)
print(list2)
print(shuffle(list1,list2))
