class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def isMagic(row, col):
            row_sum = [0] * 3
            col_sum = [0] * 3
            counts = 0
            for cur_row in range(row - 2, row + 1):
                for cur_col in range(col - 2, col + 1):
                    row_sum[cur_row - (row - 2)] += grid[cur_row][cur_col]
                    col_sum[cur_col - (col - 2)] += grid[cur_row][cur_col]

                    if grid[cur_row][cur_col] != 0:
                        counts |= 1 << (grid[cur_row][cur_col] - 1)

                    if cur_col == col and row_sum[cur_row - (row - 2)] != 15:
                        return False
                    
                    if cur_row == row and col_sum[cur_col  - (col - 2)] != 15:
                        return False

            if grid[row][col] + grid[row - 1][col - 1] + grid[row - 2][col - 2] != 15 or grid[row - 2][col] + grid[row - 1][col - 1] + grid[row][col - 2] != 15:
                return False
            
            if counts != 511:
                return False

            return True

        res = 0
        for row in range(2, m):
            for col in range(2, n):
                if isMagic(row, col):
                    res += 1
        
        return res