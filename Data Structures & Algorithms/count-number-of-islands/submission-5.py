class Solution:
    #Time: 7:52 - 
    def numIslands(self, grid: List[List[str]]) -> int:
        #U: Given a 2D grid, we have to return the number of islands. 
        # An island is formed by connecting the lands(1) and is surrounded by water(0)

        #M/P: 
            # We can use the concept of DFS to traverse through the graph. 
            # Initialize count 
            # Create an array with the possible directions(up, down, left, right)

            # Create an inner dfs function 
                # If row < 0 or col < 0 or row > len(grid) or col > len(grid[0]) or grid[row][col] == "0", 
                # that means there is water so the program does not do anything; it just returns and moves 
                # on to the next part of the grid 

                # For dr, dc in directions: 
                    # Call the dfs function on (r + dr, c + dc)
            
            # Intialize row and col to 0 
            # If grid[r][c] == 1, count += 1 
            # dfs(r, c)

            # Return count 

        #I: 
        if not grid: 
            return 0 

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == "0"
            ):
                return

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands
        