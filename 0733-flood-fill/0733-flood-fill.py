class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        stack = deque()
        stack.append((sr, sc))
        compare = image[sr][sc]
        image[sr][sc] = color
        
        if compare == color:
            return image
        
        def dfs(x, y):
            for xPlus, yPlus in directions:
                newX = x + xPlus
                newY = y + yPlus
                if newX < 0 or newX >= len(image) or newY < 0 or newY >= len(image[0]):
                    continue
                    
                if image[newX][newY] == compare:
                    image[newX][newY] = color
                    dfs(newX, newY)
            return
        
        dfs(sr, sc)
                    
        return image