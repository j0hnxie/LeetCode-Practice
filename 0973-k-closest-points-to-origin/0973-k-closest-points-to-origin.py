class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        test = []
        result = []
        for i in range(len(points)):
            xDist = points[i][0] * points[i][0]
            yDist = points[i][1] * points[i][1]
            totalDist = xDist + yDist
            res = -1 * sqrt(totalDist)
            if len(test) < k:
                heapq.heappush(test, [res, i])
            else: 
                heapq.heappushpop(test, [res, i])
            
        for i in test:
            result.append(points[i[1]])
            
        return result