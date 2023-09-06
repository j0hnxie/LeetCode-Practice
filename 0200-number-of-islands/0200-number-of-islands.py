class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        islands = 0
        
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if visited[i][j] or grid[i][j] == "0":
                    continue
                
                islands += 1
                stack = []
                stack.append([i, j])
                while stack:
                    top = stack[-1]
                    stack.pop()
                    visited[top[0]][top[1]] = True
                    for k in directions:
                        newX = top[0] + k[0]
                        newY = top[1] + k[1]
                        if newX < 0 or newY < 0 or newX >= len(grid) or newY >= len(grid[i]):
                            continue
                        
                        if not visited[newX][newY] and grid[newX][newY] == "1":
                            stack.append([newX, newY])
                    
        return islands