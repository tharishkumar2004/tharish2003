a=[]
n=int(input("no.of elements in list:"))
for i in range(1,n+1):
    b=int(input("enter element:"))
    a.append(b)
print(a)
def small(nums):
    count=[0]*len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j]<nums[i]:
                count[j]+=1
    return count
print(small(a))
