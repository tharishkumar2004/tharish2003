a=[]
n=int(input("enter the number:"))
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        a.append("fizzbuzz")
    elif i%3==0:
        a.append("fizz")
    elif i%5==0:
        a.append("buzz")
    else:
        a.append(str(i))
print(a)
