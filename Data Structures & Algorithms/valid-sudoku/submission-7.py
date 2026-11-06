class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #U: Sudoku board is valid if: 
            # each row and col contain digits 1-9 without duplicates 
            # Each of the 9 subboxes contain digits 1-9 without duplicates too 
        
        #M/P: Iterate through the board (nested for loops)
            # rows, cols, and subbox sets

        #I: 
        rows = defaultdict(set) 
        cols = defaultdict(set)
        subboxes = defaultdict(set) 

        for r in range(9): 
            for c in range(9): 
                if board[r][c] == ".": 
                    continue 

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in subboxes[(r // 3, c // 3)]: 
                    return False 
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                subboxes[(r // 3, c // 3)].add(board[r][c])
        
        return True

        #E: Time: O(n^2), Space: O(n^2)