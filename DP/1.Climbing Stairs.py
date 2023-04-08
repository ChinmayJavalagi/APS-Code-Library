# Memoization 

# TC - O(n)
# SC - O(n) [recursion stack] + O(n) [dp array]

class Solution:
    def nthFibonacci(self, n):
        dp = [-1]*(n+1)
        a = self.fib(n,dp)
        return a
        
    def fib(self,n,dp):
        if n<=1:                                                     
            return 1                                                      #for fibo return n
        if dp[n] != -1:
            return dp[n]
        dp[n] = self.fib(n-1,dp)+self.fib(n-2,dp)
        return dp[n]


# Tabulation 

# TC - O(n)
# SC - O(n) [dp array]

class Solution:
    def nthFibonacci(self, n):
        dp = [1,1]                                                       # for fibo [0,1]
        for i in range(2,n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]

# Space Optimized 

# TC - O(n)
# SC - O(1) 
class Solution:
    def nthFibonacci(self, n): 
        prev2 = 1                                                         # for fibo 0
        prev = 1
        for i in range(2,n+1):
            curi = prev2 + prev
            prev2 = prev
            prev = curi
        return prev
