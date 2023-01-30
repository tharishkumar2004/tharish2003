def countstrings(n,start):
    if n==0:
        return 1
    count=0
    for i in range(start,5):
        count+=countstrings(n-1,i)
    return count
def countvowelstrings(n):
    return countstrings(n,0)
n=int(input("enter a number:"))
print(countvowelstrings(n))
