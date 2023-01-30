n = int(input("Enter a number : "))
reversed_n = 0
    
while n >0:
    rem = n % 10
    reversed_n = reversed_n * 10 + rem
    n //= 10
if n<0:
    print("The number cannot be reversed as it is negative.")

else:
    print("Reversed Number: ",reversed_n)

    
