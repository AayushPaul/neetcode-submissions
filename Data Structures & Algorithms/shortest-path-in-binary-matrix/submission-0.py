class Solution:
    # Time: 10:04 - 10:26, 11:24 - 12:10 
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #U: I am given an n by x binary matrix grid; given that, return the shortest clear path in the matrix. 
            # The length of clear path = number of visited cells of this path 

        #M/P: BFS algorithm 
            # Edge cases: if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or (row, col) in 
            # a visited set or grid[row][col] == 1
                # Continue 

            # If row == len(grid) - 1 and col == len(grid[0]) - 1
                # Length is returned 

            # 
        
        #I: 
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        visited_cells = set() 
        queue = deque() 
        queue.append((0, 0))
        visited_cells.add((0, 0))
        length = 1

        while queue: 
            for i in range(len(queue)): 
                r, c = queue.popleft() 

                if r == ROWS - 1 and c == COLS - 1: 
                    return length 

                # Directions: north, south, east, west, northeast, northwest, southeast, southwest
                neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

                for dr, dc in neighbors: 
                    if r + dr < 0 or c + dc < 0 or r + dr >= ROWS or c + dc >= COLS or (r + dr, c + dc) in visited_cells or grid[r + dr][c + dc] == 1: 
                        continue 
                    
                    queue.append((r + dr, c + dc)) 
                    visited_cells.add((r + dr, c + dc))
            
            length += 1
        
        return -1

        #E: Time: O(n * m), Space: O(n * m) where n = # rows, m = # cols
            # Note: Both queue and set could have n * m vertices in the worst case when the grid has all zeroes. 