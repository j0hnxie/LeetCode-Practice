class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[1], x[0]))
        n = len(points)

        idx = 0
        result = 0
        while idx < n:
            current_end = points[idx][1]
            while idx < n and points[idx][0] <= current_end:
                idx += 1
            result += 1
        return result