class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here
        dp = [[0 for x in range(sum+1)] for x in range(N+1)]
       
        for i in range(N+1):
            dp[i][0] = 1
            
        for i in range(1,N+1):
            for j in range(1,sum+1):
                if j < arr[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i - 1][j-arr[i-1]]
                
        return 1 if dp[N][sum] else 0