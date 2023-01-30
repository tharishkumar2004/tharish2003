def minJumps(arr, l, h):

	if (h == l):
		return 0
	    
	if (arr[l] == 0):
		return float('inf')
	min = float('inf')
	for i in range(l + 1, h + 1):
		if (i < l + arr[l] + 1):
			jumps = minJumps(arr, i, h)
			if (jumps != float('inf') and
					jumps + 1 < min):
				min = jumps + 1

	return min


l=[]
n = int(input("Enter number of elements : "))
for i in range(n):
    l.append(int(input("Enter element"+str(i+1)+":")))
print("The orginal list is ",l)
print('Minimum number of jumps to reach the end is', minJumps( l, 0, n-1))
  
