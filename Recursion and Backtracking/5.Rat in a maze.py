"""
1. We call the solve fuction if m[0][0] is 1.
2. We iterate for 4 different directions down, left, right, up to check all the possible ways that are present if we go in that specific direction.
3. If nexti and nextj are inbound and not visited and m[nexti][nextj] == 1, then we mark the present position as visited and move forward with the next direction by adding that direction to a string got output. 
4. If we reach the last index then we have a string to append in the result.
5. Else backtrack by making the index in visited array as unvisited.
"""
# Time Complexity: O(4^(m*n)), because on every cell we need to try 4 different directions.

class Solution:
    def findPath(self, m, n):
        # code here
        def solve(i,j,move,di,dj):
            if i == n-1 and j == n-1:
                ans.append(move)
                return 
            dir = 'DLRU' #We have to return the strings in lexicographically increasing order
            for ind in range(4):
                nexti = i+di[ind]
                nextj = j+dj[ind]
                if nexti>=0 and nextj>=0 and nexti<n and nextj<n and not visited[nexti][nextj] and m[nexti][nextj]==1:
                    visited[i][j] = 1
                    solve(nexti, nextj, move+dir[ind], di, dj)
                    visited[i][j] = 0
        
        ans = []
        visited = [[0]*n for i in range(n)]
        #    d, l, r, u 
        di = [1,0,0,-1]
        dj = [0,-1,1,0]
        if m[0][0] == 1:
            solve(0,0,"",di,dj)
        return ans
