class Solution:
    #Time: 3:24 - 4:10 
    def numIslands(self, grid: List[List[str]]) -> int:
        #U: Given grid, count and return the # islands 
            # 1 represents land, 0 represents water 
        
        # M/P: 
            # Create a set that keeps track of visited nodes 
            # DFS (helper/inner function)
            # Increment count when all nodes surrounding the 1's are 0's 
        
        #I: 
        if not grid or not grid[0]: 
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
                    islands += 1
                    dfs(r, c)
                    

        return islands
        