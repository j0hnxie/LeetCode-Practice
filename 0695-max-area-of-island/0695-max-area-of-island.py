class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m = len(grid)
        n = len(grid[0])
        def dfs(i, j):
            self.area += 1
            for x, y in dirs:
                newX = i + x
                newY = j + y
                
                if newX < 0 or newY < 0 or newX >= m or newY >= n:
                    continue
                
                if grid[newX][newY] == 1:
                    grid[newX][newY] = 0
                    dfs(newX, newY)
        
        res = 0
        for i in range(m):
            for j in range(n):
                self.area = 0
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    dfs(i, j)
                res = max(self.area, res)
        return res
            