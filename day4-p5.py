n=input("enter string:")
s=""
for i in n:
    if i.isalpha():
        s+=i
if(s[::-1]==s):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
