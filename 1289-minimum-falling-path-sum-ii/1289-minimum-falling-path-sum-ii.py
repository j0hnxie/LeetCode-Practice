class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        prev = grid[0]
        
        for row in range(1, n):
            cur = [float('inf') for i in range(n)]
            for col in range(n):
                for prev_col in range(n):
                    if prev_col == col:
                        continue
                    
                    cur[col] = min(cur[col], prev[prev_col])
                cur[col] += grid[row][col]
            prev = cur
            # print(prev)
        return min(prev)