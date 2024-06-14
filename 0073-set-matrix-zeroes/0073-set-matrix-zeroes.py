class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])
        col_zero = False
    
        for row_idx, row_list in enumerate(matrix):
            for col_idx, element in enumerate(row_list):
                if element == 0:
                    matrix[row_idx][0] = 0
                    if col_idx == 0:
                        col_zero = True
                    else:
                        matrix[0][col_idx] = 0
        
        # print(matrix)
        # print(col_zero)
        
        for col_idx in range(1, n):
            if matrix[0][col_idx] == 0:
                for row_idx in range(m):
                    matrix[row_idx][col_idx] = 0
        
        for row_idx in range(m):
            if matrix[row_idx][0] == 0:
                for col_idx in range(n):
                    matrix[row_idx][col_idx] = 0
        
        if col_zero:
            for row_idx in range(m):
                matrix[row_idx][0] = 0
        
            
            
                