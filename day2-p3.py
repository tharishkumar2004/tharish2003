l=[]
n=int(input("Enter no. of sentences : "))
for i in range(n):
    l.append(input("Enter a sentence : "))
print(l,'is the list of strings.')
print()
for i in l:
    c=0
    if i!='':
        s=i.split()
        c+=len(s)
        print("There are",c,"words present in sentence",)
    else:
        print("There are",c,"words present.")
