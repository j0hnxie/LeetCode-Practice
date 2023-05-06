class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        stack = deque()
        stack.append((sr, sc))
        compare = image[sr][sc]
        image[sr][sc] = color
        
        if compare == color:
            return image
        
        while stack:
            x, y = stack.pop()
            for xPlus, yPlus in directions:
                newX = x + xPlus
                newY = y + yPlus
                if newX < 0 or newX >= len(image) or newY < 0 or newY >= len(image[0]):
                    continue
                    
                if image[newX][newY] == compare:
                    image[newX][newY] = color
                    stack.append((newX, newY))
                    
        return image