t=int(input("enter the value"))
entry=[int(input("enter the no of entry"))]
exit=int(input("enter the no of exit"))]
count=0
guest=[ ]
for i in range (len(entry)):
   count=count+entry[i]-exit[i]
   guest.append(count)
   print(max(guest))
