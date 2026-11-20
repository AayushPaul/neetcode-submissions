class Solution:
    # Time: 12:06 - 1:02  
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #M/P: BFS 
            # 1. Handle the edge cases: 
                # - If either the first cell on the top left or the last cell on the bottom right has value of 1, program returns -1. 
                # - If the grid only has one cell (1 x 1 grid), program returns 1
            
            # 2. Initialize a queue with (0, 0), a visited set with (0, 0), length = 1

            # 3. Run BFS level by level. For each cell, we have to check all 8 directions. Skip anything that is out of bounds, value 
            # in the new cell is 1, or cell is already visited. 

            # 4. If valid neighbor is basically the last cell or n - 1, then return length + 1 immediately to avoid more work 

            # 5. After each level finishes, increment length. If the queue empties without reaching target, return -1. 

            # Time: O(n^2), 

        #I: 
        lastCellIdx = len(grid) - 1
        if grid[0][0] == 1 or grid[lastCellIdx][lastCellIdx] == 1: 
            return -1 
        
        if lastCellIdx == 0:
            return 1

        queue, visitedCells = deque(), set()
        queue.append((0, 0))
        visitedCells.add((0, 0))
        length = 1 

        while queue: 
            directions = [[1, 0], [-1, 0], [0, -1], [0, 1], [1, -1], [1, 1], [-1, -1], [-1, 1]]
            for _ in range(len(queue)):
                row, col = queue.popleft() 
                for dr, dc in directions: 
                    if row + dr < 0 or col + dc < 0 or row + dr > lastCellIdx or col + dc > lastCellIdx or grid[row + dr][col + dc] == 1 or (row + dr, col + dc) in visitedCells: 
                        continue 

                    if row + dr == lastCellIdx and col + dc == lastCellIdx: 
                        return length + 1
                        
                    queue.append((row + dr, col + dc)) 
                    visitedCells.add((row + dr, col + dc))

            length += 1

        return -1

        #R: grid = [[0, 1], 
            #      [1, 0]]

            # queue = (), visited = {(0, 0)}, length = 1