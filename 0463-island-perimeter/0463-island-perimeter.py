class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    right, left, up, down = 0, 0, 0, 0
                    
                    if c == col - 1 or grid[r][c + 1] == 0:
                        right += 1
                    
                    if c == 0 or grid[r][c - 1] == 0:
                        left += 1
                    
                    if r == row - 1 or grid[r + 1][c] == 0:
                        down += 1
                    
                    if r == 0 or grid[r - 1][c] == 0:
                        up += 1
                    res += (right + left + down + up)
        return res
                    