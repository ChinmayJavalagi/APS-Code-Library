# TC - O(n*m)
# SC - O(n*m)

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, values, n):
        
        r = n
        c = W
        
        dp = [[0]*(c+1) for _ in range(r+1)]
        
        for i in range(1,r+1):
            for j in range(1, c+1):
                if wt[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], values[i-1]+dp[i-1][j-wt[i-1]])
        return dp[-1][-1]
