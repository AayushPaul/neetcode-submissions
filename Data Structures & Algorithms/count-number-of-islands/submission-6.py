class Solution:
    #Time: 5:45 - 6:26 
    def numIslands(self, grid: List[List[str]]) -> int:
        #U: Given 2D grid where '1' represents land and '0' represents water, count and return the number of islands. 

        #M/P: 4 possible directions that robot can travel on each piece of grid is up, down, left, and right 
            # directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            # DFS Helper function 
                # If r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0": 
                    # return 

                # grid[r][c] = "0"
                # For loop to go through all 4 directions (for dr, dc in directions)
                    # dfs(r + dr, c + dc)

            # Write a nested for loop for the robot to go through each row and col 
                # When a 1 is encountered, an island is encountered (if statement) 
                    # DFS is performed on each piece of the grid 
                    # islands += 1

        #I: 
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0 
        numRows, numCols = len(grid), len(grid[0])

        def dfs(r, c): 
            if r < 0 or r >= numRows or c < 0 or c >= numCols or grid[r][c] == "0": 
                return 

            grid[r][c] = "0"
            for dr, dc in directions: 
                newRow, newCol = r + dr, c + dc
                dfs(newRow, newCol)

        for row in range(numRows): 
            for col in range(numCols): 
                if grid[row][col] == "1": 
                    dfs(row, col) 
                    islands += 1

        return islands 

        #R: Example 2

        #E: Time: O(m * n), Space: O(m * n)