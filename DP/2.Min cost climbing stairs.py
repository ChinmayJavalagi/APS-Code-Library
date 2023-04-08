
#TC - O(n)
#SC - O(n)

#Can be space optimised furthur

class Solution:
    def minCostClimbingStairs(self, cost, N):
        #Write your code here
        cost.append(0)
        for i in range(N-3, -1,-1):
            cost[i] = min(cost[i+1], cost[i+2])+cost[i]
            
        return min(cost[0], cost[1])
        
