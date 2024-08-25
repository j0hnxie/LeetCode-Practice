class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows = [0] * m
        cols = [0] * n

        convert = {}
        for row in range(m):
            for col in range(n):
                convert[mat[row][col]] = (row, col)
        
        for idx, num in enumerate(arr):
            row, col = convert[num]
            rows[row] += 1
            cols[col] += 1

            if rows[row] == n or cols[col] == m:
                return idx
        return -1