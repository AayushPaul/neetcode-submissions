class Solution:
    # Time: 1:30 -  
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
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