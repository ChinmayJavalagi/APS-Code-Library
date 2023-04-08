#TC - O(amount*len(coins))
#SC = O(amount)

class Solution(object):
    def coinChange(self, coins, amount):
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        
        for a in range(1,amount+1):
            for c in coins:
                if c<=a:
                    dp[a] = min(1+dp[a-c], dp[a])
        
        return dp[amount] if dp[amount] != amount+1 else -1 
