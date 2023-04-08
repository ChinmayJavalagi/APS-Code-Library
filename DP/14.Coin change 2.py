#TC - O(n*m)
#SC - O(n*m)


class Solution(object):
    def change(self, amount, coins):
        N = len(coins)
        dp = [[0 for i in range(amount+1)]for j in range(N)]
        for i in range(N):
            dp[i][0] = 1
        
        for i in range(N):
            for j in range(1,amount+1):
                if coins[i]>j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
                
        return dp[-1][-1]
