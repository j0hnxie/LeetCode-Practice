class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = [[0 for _ in range(n)] for _ in range(m)]
        memo[0][0] = grid[0][0]

        for col in range(1, n):
            memo[0][col] = memo[0][col - 1] + grid[0][col]
        
        for row in range(1, m):
            memo[row][0] = memo[row - 1][0] + grid[row][0]
        
        for row in range(1, m):
            for col in range(1, n):
                memo[row][col] = min(memo[row - 1][col], memo[row][col - 1]) + grid[row][col]
        
        # print(memo)
        return memo[-1][-1]