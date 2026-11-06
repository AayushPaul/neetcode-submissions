class Solution:
    # Time: 3:02 - 
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #U: Return true if the Soduku board is valid, false otherwise 

        #M/P: Hashset for each row, col, and sqaure

        #I: 
        rows = defaultdict(set) 
        cols = defaultdict(set) 
        squares = defaultdict(set) 

        for row in range(9): 
            for col in range(9): 
                square_key = (row // 3, col // 3)
                currElem = board[row][col]

                if currElem in rows[row] or currElem in cols[col] or currElem in squares[square_key]: 
                    return False
                
                if currElem == ".": 
                    continue 

                rows[row].add(currElem)
                cols[col].add(currElem)
                squares[square_key].add(currElem)
        
        return True 

        #E: Time: O(81) or O(1), Space: O(81) or O(1)