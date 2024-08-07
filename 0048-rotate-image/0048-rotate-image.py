class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix) - 1
        upper = math.ceil(len(matrix) / 2)
        lower = len(matrix) // 2
        for row in range(upper):
            for col in range(lower):
                # print(str(row) + " " + str(col))
                temp = matrix[row][col]
                matrix[row][col] = matrix[n - col][row]
                matrix[n - col][row] = matrix[n - row][n - col]
                matrix[n - row][n - col] = matrix[col][n - row]
                matrix[col][n - row] = temp
                # print(matrix)

