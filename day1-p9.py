list=[]
print(list)
#addition of element in the  list using function
list.append(1)
list.append(2)
list.append(4)
print("list after addition of three elements")
list.insert(2,12)
list.pop()
print(list)
#adding element to the list using iterator
for i in range(1,4):
    list.append(i)
print(list)
#addition of list to a list
list2=["for","sample"]
list.append(list2)
print(list)
