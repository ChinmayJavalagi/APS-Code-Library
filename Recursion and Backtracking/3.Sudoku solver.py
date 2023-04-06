"""
1. Run two for loops to get access to the board[r][c].
2. If the board[r][c] is empty then we have to start checking which number would fit.
3. We run a for loop from 1 to 9 and check isPossible.
        isPossible--> true, then fill the board[r][c] with num, check if the backtrack fucntion returns True, if yes then return True, else, do backtracking and reassign the board[r][c] as empty.

Note: Comments for isPossible function is written in that function itself.
"""

# Time Complexity: O(9(n ^ 2)), in the worst case, for each cell in the n2 board, we have 9 possible numbers.

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def backtrack(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            if isPossible(i, j, num):
                                board[i][j] = num
                                if backtrack(board):
                                    return True
                                else:
                                    board[i][j] = '.'
                        return False
            return True

        def isPossible(r, c, nums):
            for i in range(9):
                #check in the column
                if board[r][i] == nums: return False
                #check in the row
                if board[i][c] == nums: return False
                #check in the box 3x3
                if board[3*(r//3) + i//3][3*(c//3) + i%3] == nums: return False
            return True

        return backtrack(board)
