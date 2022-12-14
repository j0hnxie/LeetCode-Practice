class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        
        bfs = deque()
        visited = set()
        maxDist = len(mat) + len(mat[0])
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    bfs.append((i, j))
                    visited.add((i, j))
                else:
                    mat[i][j] = maxDist
            
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dist = 0
        # print(str(i) + " " + str(j))
        while bfs:
            # print(bfs)
            size = len(bfs)
            for k in range(size):
                cur = bfs.popleft()
                visited.add((cur[0], cur[1]))
                mat[cur[0]][cur[1]] = min(dist, mat[cur[0]][cur[1]])
                for direction in directions:
                    newY = cur[0] + direction[0]
                    newX = cur[1] + direction[1]
                    if (newY, newX) not in visited:
                        if newY < 0 or newY >= len(mat):
                            continue
                        elif newX < 0 or newX >= len(mat[0]):
                            continue
                        bfs.append((newY, newX))
            dist += 1
                
        return mat
                
                            
                    