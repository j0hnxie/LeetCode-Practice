class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        m = len(heights)
        n = len(heights[0])
        
        pQ = deque()
        aQ = deque()
        aQVisit = set()
        pQVisit = set()
        for i in range(m):
            pQ.append((i, 0))
            pQVisit.add((i, 0))
            aQ.append((i, n - 1))
            aQVisit.add((i, n - 1))
            
        for i in range(n):
            pQ.append((0, i))
            pQVisit.add((0, i))
            aQ.append((m - 1, i))
            aQVisit.add((m - 1, i))
        
        while pQ:
            x, y = pQ.pop()
            
            for i, j in dirs:
                newX = x + i
                newY = y + j
                
                if newX < 0 or newY < 0 or newX >= m or newY >= n:
                    continue
                
                if (newX, newY) in pQVisit:
                    continue
                    
                if heights[newX][newY] < heights[x][y]:
                    continue
                
                pQVisit.add((newX, newY))
                pQ.append((newX, newY))
        
        while aQ:
            x, y = aQ.pop()
            
            for i, j in dirs:
                newX = x + i
                newY = y + j
                
                if newX < 0 or newY < 0 or newX >= m or newY >= n:
                    continue
                    
                if (newX, newY) in aQVisit:
                    continue
                
                if heights[newX][newY] < heights[x][y]:
                    continue
                
                aQVisit.add((newX, newY))
                aQ.append((newX, newY))
        
#         print(aQVisit)
#         print(pQVisit)
        
        return list(pQVisit.intersection(aQVisit))