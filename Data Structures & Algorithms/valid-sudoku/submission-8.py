class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #U: Sudoku board is valid if: 
            # Each row must contain the digits 1-9 without duplicates
            # Each column must contain digits 1-9 without duplicates 

            # Each of the nine 3x3 subboxes of the grid must contain the digits 1-9 without duplicates 

        #M/P: Create sets for rows, cols, and 3x3 subboxes (no duplicates) 
        
            # If a duplicate is found in a row, col, or subbox, return False 
            # Otherwise, return True 

        #I: 
        rows = defaultdict(set) 
        cols = defaultdict(set) 
        squares = defaultdict(set) 

        for r in range(9): 
            for c in range(9): 
                if board[r][c] == ".": 
                    continue 

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]: 
                    return False 

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])  # This causes the space complexity to also be O(n^2)
        
        return True

        #E: Time: O(n^2), Space: O(n^2)