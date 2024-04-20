class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m = len(land)
        n = len(land[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        res = []
        for row in range(m):
            for col in range(n):
                if land[row][col] == 1:
                    cur = [float('inf'), float('inf'), -1, -1]
                    stack = [(row, col)]
                    while stack:
                        x, y = stack.pop()
                        cur[0] = min(cur[0], x)
                        cur[2] = max(cur[2], x)
                        cur[1] = min(cur[1], y)
                        cur[3] = max(cur[3], y)
                        
                        for add_x, add_y in dirs:
                            new_x = x + add_x
                            new_y = y + add_y
                            
                            if new_x < 0 or new_y < 0 or new_x >= m or new_y >= n:
                                continue
                                
                            if land[new_x][new_y] == 0:
                                continue
                            
                            stack.append((new_x, new_y))
                            land[new_x][new_y] = 0
                    res.append(cur)
        
        return res