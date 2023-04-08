# TC - O(a*b)
# SC - O(a*b)

class Solution(object):
    def uniquePaths(self, a, b):
        matrix = [[1 for i in range(b)] for j in range(a)]
        for i in range(a-2,-1,-1):
            for j in range(b-2,-1,-1):
                matrix[i][j] = matrix[i+1][j] + matrix[i][j+1]
        return matrix[0][0]
