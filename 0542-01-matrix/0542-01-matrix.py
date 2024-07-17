class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
     
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] != 0:
                    mat[i][j] = float('inf')
                    if i > 0:
                        mat[i][j] = min(mat[i][j], mat[i - 1][j] + 1)
                    if j > 0:
                        mat[i][j] = min(mat[i][j], mat[i][j - 1] + 1)
        
        for i in range(len(mat) - 1, -1, -1):
            for j in range(len(mat[i]) - 1, -1, -1):
                if mat[i][j] != 0:
                    if i < len(mat) - 1:
                        mat[i][j] = min(mat[i][j], mat[i + 1][j] + 1)
                    if j < len(mat[i]) - 1:
                        mat[i][j] = min(mat[i][j], mat[i][j + 1] + 1)
        
        return mat   