class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        compare = image[sr][sc]

        if compare == color:
            return image

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        visited.add((sr, sc))

        def helperDFS(image, sr, sc, color, compareColor):
            if image[sr][sc] == compareColor:
                image[sr][sc] = color
                visited.add((sr, sc))
            else:
                return image

            
            for direction in directions:
                newR = sr + direction[0]
                newC = sc + direction[1]

                if newR >= 0 and newR < len(image) and newC >= 0 and newC < len(image[0]):
                    if (newR, newC) not in visited:
                        helperDFS(image, newR, newC, color, compareColor)
            
            return image

        image = helperDFS(image, sr, sc, color, compare)
        return image

