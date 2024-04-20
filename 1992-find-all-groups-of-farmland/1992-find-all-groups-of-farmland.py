class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m = len(land)
        n = len(land[0])
        
        res = []
        for row in range(m):
            for col in range(n):
                if land[row][col] == 1:
                    cur = [row, col]
                    x = row
                    y = col
                    while x < m and land[x][col] == 1:
                        y = col
                        while y < n and land[x][y] == 1:
                            land[x][y] = 0
                            y += 1
                        x += 1
                    cur.append(x - 1)
                    cur.append(y - 1)
                    res.append(cur)
        return res