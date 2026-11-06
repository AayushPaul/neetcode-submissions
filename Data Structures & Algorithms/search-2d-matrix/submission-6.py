class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #U: I am given an m * n 2D integer array matrix and integer target 
            # Each row in matrix is sorted in non-decreasing order 
            # The first integer of every row is greater than the last integer of the previous row.
        
        # Return true if target exists within matrix or false otherwise 

        # Required time complexity: O(log(m * n)) 

        #M/P: Binary Search 
            # Do binary search on the rows (uses the 2nd property)
                # correctRow = (top + bottom) // 2
                # If target > last elem in correctRow 
                    # top = correctRow + 1
                # else if target < first elem in correctRow 
                    # bottom = correctRow - 1
                # else 
                    # break (target is in correct row now)
            
            # If top row index > bottom row index, target is not in the matrix (program returns false)

            # Do binary search within the correct row and determine if target exists within that row. 
            # If target exists in the row, return True. 

        #I: 
        top, bottom = 0, len(matrix) - 1    # variables for row indices; len(matrix) = # rows

        while top <= bottom: 
            correctRow = (top + bottom) // 2
            if target > matrix[correctRow][-1]: 
                top = correctRow + 1
            elif target < matrix[correctRow][0]: 
                bottom = correctRow - 1
            else: 
                break 
        
        if top > bottom: 
            return False 
        
        l, r = 0, len(matrix[0]) - 1    # len(matrix[0]) = # cols 
        while l <= r: 
            mid = (l + r) // 2
            if target > matrix[correctRow][mid]: 
                l = mid + 1
            elif target < matrix[correctRow][mid]: 
                r = mid - 1
            else: 
                return True # target is found 
        
        return False 
        
        #R: Example 1
        # top, bottom = 0, rows - 1
        
        #E: Time: O(log(m)*log(n)) = O(log(m * n)), Space: O(1)