# TC - O(N)
# SC - (1)


class Solution(object):
    def maxProfit(self, prices):
        maxi, mini = 0, prices[0]
        for i in range(1,len(prices)+1):
            maxi = max(maxi, prices[i-1] - mini)
            mini = min(mini, prices[i-1])
        return maxi        
