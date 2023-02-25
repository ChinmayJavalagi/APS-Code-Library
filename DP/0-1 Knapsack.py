class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        
        matrix = [[0 for i in range(W+1)]for j in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,W+1):
                if j<wt[i-1]:
                    matrix[i][j] = matrix[i-1][j]
                else:
                    matrix[i][j] = max(matrix[i-1][j], val[i-1]+matrix[i-1][j-wt[i-1]])
            
        return matrix[n][W]