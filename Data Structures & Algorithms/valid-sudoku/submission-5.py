class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #U: Determine if the sudoku board is valid or not 
        #based on the three conditions(no duplicates in rows, columns, 
        #subboxes)

        #M: defaultdict of sets, arrays

        #P: 
            #1. Initialize three sets with defaultdict(three conditions)
            #2. Create nested for loops that iterate through rows and cols
                #3. if [row][col] == ".": continue 
                #4. Check if any box has duplicates based on the three conditions
                    #5. If so, return False. 
                #5. If not, add the corresponding numbers to row, col, and subbox while the program 
                #goes through all the rows and cols 
            
            #6. Return True at end of program. 
        
        #I: 
        rows = defaultdict(set)
        cols = defaultdict(set)
        subboxes = defaultdict(set)

        for row in range(9): 
            for col in range(9): 
                
                #Checking if the space is empty
                if board[row][col] == ".": 
                    continue

                #Checking for any duplicates
                if ((board[row][col] in rows[row]) or (board[row][col] in cols[col]) or 
                (board[row][col] in subboxes[(row // 3, col // 3)])): 
                        return False
                
                #Adds the corresponding elements at a row and col to all 3 sets
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                subboxes[(row // 3, col // 3)].add(board[row][col])
        
        return True 
                
                



                


        