class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visit = set()
        area = 0

        def dfs(r, c): 
            if (r not in range(rows) or c not in range(columns) or (r,c) in visit or grid[r][c] == 0): 
                return 0
            
            visit.add((r, c))

            result = 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            return result 
        
        for r in range(rows): 
            for c in range(columns): 
                if (grid[r][c] == 1 or (r, c) not in visit): 
                    area = max(area, dfs(r, c))
        
        return area
