l=[]
n=int(input("enter the number:"))
for i in range(n):
    e=int(input("enter the element:"))
    l.append(e)
print("the orginal list is",1)
odd=0
even=0
for i in l:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("the number of odd number in the list are",odd)
print("the number of even number in the list are",even)
