class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def dfs(row, col):
            for dx, dy in dirs:
                new_row, new_col = row + dx, col + dy
                if new_row < 0 or new_col < 0 or new_row >= (n * 3) or new_col >= (n * 3):
                    continue
                
                if big_grid[new_row][new_col] == 1:
                    continue

                big_grid[new_row][new_col] = 1
                dfs(new_row, new_col)

        n = len(grid)
        big_grid = [[0] * (n * 3) for _ in range(n * 3)]
        for row in range(n):
            for col in range(n):
                char = grid[row][col]
                big_row = row * 3
                big_col = col * 3
                if char == "/":
                    big_grid[big_row + 2][big_col] = 1
                    big_grid[big_row + 1][big_col + 1] = 1
                    big_grid[big_row][big_col + 2] = 1
                elif char == "\\":
                    big_grid[big_row][big_col] = 1
                    big_grid[big_row + 1][big_col + 1] = 1
                    big_grid[big_row + 2][big_col + 2] = 1
        
        res = 0
        for row in range(n * 3):
            for col in range(n * 3):
                if big_grid[row][col] == 0:
                    big_grid[row][col] = 1
                    dfs(row, col)
                    res += 1
        return res
