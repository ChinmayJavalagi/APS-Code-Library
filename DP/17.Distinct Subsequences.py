#Top Down approach
#TC - O(n*m)

class Solution(object):
    def numDistinct(self, s, t):
        n = len(s)
        m = len(t)
        dp = [[0]*(m+1) for i in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 1
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j]+dp[i-1][j-1]
                
                else:
                    dp[i][j] = dp[i-1][j]
                print(dp[i][j])
            print('\n')
        return dp[n][m]%1000000007
      
      
      
#Memoization
#TC - O(n*m)


class Solution(object):
    def numDistinct(self, s, t):
        m = len(s)
        n = len(t)
        dp = {}

        def dfs(i,j):
            if j == n:
                return 1
            if i == m:
                return 0
                
            if (i,j) in dp:
                return dp[(i,j)]
            if s[i] == t[j]:
                dp[(i,j)] = dfs(i+1, j+1) + dfs(i+1,j)
            else:
                dp[(i,j)] = dfs(i+1, j)
            return dp[(i,j)]
        return dfs(0,0)

