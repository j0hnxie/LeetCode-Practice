class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bfs = deque()
        nonRot = set()
        minutes = 0
        add = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    bfs.append((i, j))
                    nonRot.add((i, j))
                elif grid[i][j] == 1:
                    nonRot.add((i, j))
        
        while bfs:
            curLen = len(bfs)
            for i in range(curLen):
                cur = bfs.popleft()
                nonRot.discard((cur[0], cur[1]))
                
                for j in add:
                    newX = cur[0] + j[0]
                    newY = cur[1] + j[1]
                    
                    if newX < 0 or newX >= len(grid):
                        continue
                    if newY < 0 or newY >= len(grid[0]):
                        continue
                    if grid[newX][newY] != 1:
                        continue
                    
                    grid[newX][newY] = 2
                    bfs.append((newX, newY))
                    
                
            minutes += 1
        
        if nonRot:
            return -1
        else:
            return minutes - 1 if minutes else minutes
            