class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #U: Return true if target exists within matrix; False otherwise 

        #M/P: 
            #Binary search: O(logn)
        
        #I: 

        #Optimal/Binary Search Approach 
        #1. Perform binary search over the rows to find a potential row where the target might be in 
        #2. Perform binary search within the potential row to find the target 

        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1

        #Binary search over all the rows 
        while top <= bottom: 
            midRow = (top + bottom) // 2

            if target > matrix[midRow][-1]: 
                top = midRow + 1
            elif target < matrix[midRow][0]: 
                bottom = midRow - 1
            else: 
                break 

        if not top <= bottom: 
            return False 
        
        left, right = 0, cols - 1
        row = (top + bottom) // 2

        #Binary search over the columns in the potential row 
        while left <= right: 
            mid = (left + right) // 2

            if target > matrix[row][mid]: 
                left = mid + 1
            elif target < matrix[row][mid]: 
                right = mid - 1
            else: 
                return True 

        return False 

        #Time: O(log(m * n)), Space: O(1)