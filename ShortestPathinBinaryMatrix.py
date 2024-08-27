class Solution:
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        rows, cols = len(grid), len(grid[0])
        
    