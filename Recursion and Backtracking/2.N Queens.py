"""
1. We start with the column 0, for every row of that column we check if it isSafe to place the queen there.
2. If yes, we place the queen at the row, col and call backtrack for next column so that we can place another queen.
3. If we reach a condition where col becomes n then we have our board with n queens placed. so we append and return back to find other boards.
"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        res = ['.'*n for i in range(n)]
        ans = []
        def backtrack(col):
            if col == n:
                ans.append(res[:])
                return 

            for row in range(n):
                if(issafe(row,col)):
                    res[row] = res[row][:col] + 'Q' + res[row][col+1:]
                    backtrack(col+1)
                    res[row] = res[row][:col] + '.' + res[row][col+1:]
            return ans
        
        def issafe(r, c):
            ar = r
            ac = c
            while c>=0 and r<n:
                if res[r][c] == 'Q': return False
                r+=1
                c-=1
            
            r,c = ar,ac
            while c>=0 and r>=0:
                if res[r][c] == 'Q': return False
                r-=1
                c-=1

            r,c = ar,ac
            while c>=0:
                if res[r][c] == 'Q': return False
                c-=1    
            
            return True
        
        backtrack(0)
        return ans
