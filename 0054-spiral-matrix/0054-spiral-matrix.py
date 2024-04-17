class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = 101
        cur_dir = 0
        cur_row = 0
        cur_col = 0
        res = [matrix[0][0]]
        matrix[0][0] = visited
        
        while len(res) < m * n:
            while True:
                next_row = cur_row + dirs[cur_dir][0]
                next_col = cur_col + dirs[cur_dir][1]
                if next_row >= m or next_col >= n or next_row < 0 or next_col < 0:
                    break
                
                if matrix[next_row][next_col] == visited:
                    break
                
                res.append(matrix[next_row][next_col])
                matrix[next_row][next_col] = visited
                cur_row, cur_col = next_row, next_col
            cur_dir += 1
            cur_dir %= 4
        return res