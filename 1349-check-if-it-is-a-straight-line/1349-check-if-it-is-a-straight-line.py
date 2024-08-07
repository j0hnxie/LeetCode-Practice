class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x_one, y_one = coordinates[0]
        x_two, y_two = coordinates[1]
        dx, dy = x_two - x_one, y_two - y_one
        n = len(coordinates)

        for idx in range(2, n):
            x, y = coordinates[idx]
            if dx * (y - y_one) != dy * (x - x_one):
                return False
        return True