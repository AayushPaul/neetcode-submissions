class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Determines if the grid is even valid 
        if not grid or not grid[0]: 
            return 0
        
        islands = 0 #Counter variable 
        visit = set() #Set that keeps track of visited nodes 
        rows, cols = len(grid), len(grid[0])

        #Depth first search algorithm 
        def dfs(r, c): 
            if ((r not in range(rows)) or (c not in range(cols))
                or (grid[r][c] == "0") or (r, c) in visit): 
                return
            
            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions: 
                dfs(r + dr, c + dc)
        
        for r in range(rows): 
            for c in range(cols): 
                if (grid[r][c] == "1") and ((r, c) not in visit): 
                    islands += 1
                    dfs(r, c)
        
        return islands 