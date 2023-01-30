def combination(l):
    for i in range(len(l)):
        for j in range(len(l)):
            for k in range(len(l)):
                if i!=j and j!=k and k!=i:
                    print(l[i],l[j],l[k])
l=[]
n=int(input("Enter number of elements : "))
for i in range(n):
    l.append(int(input("Enter value"+str(i+1)+":")))
print(l,'is the list containing values.')
combination(l)
