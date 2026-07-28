class Solution(object):
    def equalPairs(self, grid):
        rows = {}
        
        for row in grid:
            row = tuple(row)
            rows[row] = rows.get(row, 0) + 1
        
        count = 0
        
        for j in range(len(grid)):
            col = tuple(grid[i][j] for i in range(len(grid)))
            count += rows.get(col, 0)
        
        return count