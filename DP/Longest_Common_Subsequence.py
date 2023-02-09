class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        matrix = [[None for i in range(y+1)] for j in range(x+1)]
        for i in range(x+1):
            matrix[i][0] = 0
        for j in range(y+1):
            matrix[0][j] = 0
        
        for i in range(1,x+1):
            for j in range(1,y+1):
                if s1[i-1] == s2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]+1
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
                    
                
        return matrix[x][y]
    
#link: https://practice.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1