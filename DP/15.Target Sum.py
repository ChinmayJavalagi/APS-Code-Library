# Memoisation
# TC - O(n*m)   n=len(nums)  m=target
# SC - O(n*m)


class Solution(object):
    def findTargetSumWays(self, arr, target):
       
        dp = {}
        
        def dfs(i, total):
            if i == len(arr):
                return 1 if total == target else 0
            if  (i, total) in dp:
                return dp[(i, total)]
                
            dp[(i, total)] = dfs(i+1, total+arr[i]) + dfs(i+1, total-arr[i])
            
            return dp[(i, total)]
        return dfs(0, 0)
