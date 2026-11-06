class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #U: Return max area of island in grid - 0 represents water and 1 represents land. 
        
        #M/P: If not grid, return 0 
        # DFS search (inner function) 
        # Keep track of max area using max function

        # Create nested for loops that traverses through the grid(row, col) 
        # Call dfs function in inner for loop 
        # Determine max area in inner for loop 
        # Return maxArea after program goes through the grid 

        #I: 
        if not grid or not grid[0]: 
            return 0 
        
        maxArea = 0 
        visited = set() 
        
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col): 
            if min(row, col) < 0 or row == ROWS or col == COLS or (row, col) in visited or grid[row][col] == 0: 
                return 0 
        
            visited.add((row, col))

            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

        for row in range(ROWS): 
            for col in range(COLS): 
                if grid[row][col] == 1 and (row, col) not in visited: 
                    area = dfs(row, col)
                    maxArea = max(maxArea, area)
        
        return maxArea 

        #Time: O(n * m), Space: O(n * m)
