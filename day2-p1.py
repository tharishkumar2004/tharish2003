'''
1. You are climbing a staircase. It takes n steps to reach the top. Each time you can either 
climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

def fib(n,dp):
    if n<=1:
        return 1
    if dp[n]!=1:
        return dp[n]
    dp[n] = fib(n-1,dp)+fib(n-2,dp)
    return dp[n]
def countways(n):
    dp=[1 for i in range(n+1)]
    fib(n,dp)
    return dp[n]

n=int(input("Enter number of steps : "))
print("Number of ways = ",countways(n))
