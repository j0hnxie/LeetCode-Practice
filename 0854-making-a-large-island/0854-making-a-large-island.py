class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        sizes = [[0] * n for _ in range(n)]
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        result = 0
        perimeter = set()
        visited = set()

        def dfs(cur_row, cur_col, visited):
            size = 1
            for d_row, d_col in dirs:
                new_row, new_col = cur_row + d_row, cur_col + d_col

                if new_row < 0 or new_col < 0 or new_row >= n or new_col >= n:
                    continue
                
                if (new_row, new_col) in visited:
                    continue
                    

                if grid[new_row][new_col] == 0:
                    perimeter.add((new_row, new_col))
                else:
                    visited.add((new_row, new_col))
                    size += dfs(new_row, new_col, visited)
            return size

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1 and (row, col) not in visited:
                    perimeter = set()
                    visited.add((row, col))
                    size = dfs(row, col, visited)

                    result = max(size, result)

                    for cur_row, cur_col in perimeter:
                        sizes[cur_row][cur_col] += size
                        result = max(result, sizes[cur_row][cur_col] + 1)

        return max(1, result)