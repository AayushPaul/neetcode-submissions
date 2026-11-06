class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #U: Return true if target exists within matrix; False otherwise 

        #M/P: 
            #Binary search: O(logn)
        
        #I: 
        
        #Brute Force 
        rows, cols = len(matrix), len(matrix[0])

        if not matrix or not matrix[0]: 
            return False 

        for row in range(rows): 
            for col in range(cols): 
                if matrix[row][col] == target: 
                    return True 
        
        return False 

        #Optimal/Binary Search Approach 
        # left, right = matrix[0], matrix[-1]

        # while left <= right: 
        #     if target in left or target in right: 
        #         return True 
