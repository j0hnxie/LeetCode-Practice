class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        m = len(grid)
        n = len(grid[0])
        def dfs(x, y):
            grid[x][y] = "0"
            for move in moves:
                newX = x + move[0]
                newY = y + move[1]
                
                if newX < 0 or newX >= m or newY < 0 or newY >= n:
                    continue
                
                if grid[newX][newY] == "1":
                    dfs(newX, newY)
        
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res