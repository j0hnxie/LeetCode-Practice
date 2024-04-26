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
            print(prev)
        # return min(prev)
        n = len(grid)
        
        if n == 1:
            return grid[0][0]
        
        prev = grid[0]
        
        min_val = float('inf')
        min_col = -1
        second_min_val = float('inf')
        second_min_col = -1
        
        for idx, val in enumerate(grid[0]):
            if val <= min_val:
                second_min_val = min_val
                second_min_col = min_col
                min_val = val
                min_col = idx
            elif val <= second_min_val:
                second_min_val = val
                second_min_col = idx
        
        for row in range(1, n):
            cur = [0] * n
            t_second_min_val = float('inf')
            t_second_min_col = -1
            t_min_val = float('inf')
            t_min_col = -1
            for idx in range(n):
                if idx == min_col:
                    cur[idx] += second_min_val
                else:
                    cur[idx] += min_val
                cur[idx] += grid[row][idx]
                
                val = cur[idx]
                if val <= t_min_val:
                    print(f"{val} less than {t_min_val} and {t_second_min_val}")
                    t_second_min_val = t_min_val
                    t_second_min_col = t_min_col
                    t_min_val = val
                    t_min_col = idx
                elif val <= t_second_min_val:
                    print(f"{val} only less than {t_min_val} and {t_second_min_val}")
                    t_second_min_val = val
                    t_second_min_col = idx
            prev = cur
            min_val = t_min_val
            min_col = t_min_col
            second_min_val = t_second_min_val
            second_min_col = t_second_min_col
            print(prev)
            print(t_min_val)
            print(t_min_col)
            print(t_second_min_val)
            print(t_second_min_col)
        return min_val