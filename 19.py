#counting number
n=int(input("enter the number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("the number of digits in the number are:",count)
