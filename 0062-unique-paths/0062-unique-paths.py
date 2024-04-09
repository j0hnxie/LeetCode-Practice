class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = [[1] * (n) for i in range(m)]
        
        for row in range(1, m):
            for col in range(1, n):
                memo[row][col] = memo[row - 1][col] + memo[row][col - 1]
        
        return memo[m - 1][n - 1]