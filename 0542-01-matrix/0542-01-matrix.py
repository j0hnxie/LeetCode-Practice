class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        
        result = [ [float('inf')] * len(mat[0]) for i in range(len(mat))]
        queue = deque()
        for i in range(len(result)):
            for j in range(len(result[i])):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append([i, j])
                        
        dirs = [[-1 , 0], [1, 0], [0, 1], [0, -1]]
        while queue:
            cur = queue.popleft()
            row = cur[0]
            col = cur[1]
            for i in dirs:
                newRow = row + i[0]
                if newRow < 0 or newRow >= len(mat):
                    continue
                newCol = col + i[1]
                if newCol < 0 or newCol >= len(mat[row]):
                    continue
                if result[newRow][newCol] > result[row][col] + 1:
                    result[newRow][newCol] = result[row][col] + 1
                    queue.append([newRow, newCol])
                    
        return result