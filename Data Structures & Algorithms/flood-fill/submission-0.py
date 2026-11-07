class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #U: To perform flood fill,
        # 1. Begin with the starting pixel and change its color to color. 
        # 2. Perform the same process for each pixel that is directly adjacent and shares the same color as the starting pixel. 
        # 3. Repeat this process until there are no more adjacent pixels of the original color to update. 
        # 4. Retrun the modified image after performing the flood fill. 
    
        #M/P: Note - image is m x n matrix 
            # m = len(image), n = len(image[0])
            # originalVal = image[sr][sc]
                # Create dfs helper function 
                    # Edge Cases: if image[r][c] != originalVal or r < 0 or r >= m or c < 0 or c >= n
            
        #I:
        originalVal = image[sr][sc] # starting val 

        if originalVal == color: 
            return image 

        m, n = len(image), len(image[0])
        
        def dfs(r, c): 
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != originalVal: 
                return 
            else: 
                image[r][c] = color  
                
            dfs(r + 1, c) # North 
            dfs(r - 1, c) # South
            dfs(r, c + 1) # East 
            dfs(r, c - 1) # West  
        
        dfs(sr, sc) 
        return image 

        #R: Example 1
            # originalVal = 1
        
        #E: Time: O(4^(m * n)), Space: O(m * n)