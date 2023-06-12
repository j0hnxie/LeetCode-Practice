class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        test = []
        for i in range(len(points)):
            test.append([-1 * (points[i][0] * points[i][0] + points[i][1] * points[i][1]), i])
            
        heapify(test)
        
        # print(test)
        
        while len(test) > k:
            heapq.heappop(test)
            
        
        result = []    
        for i in test:
            result.append(points[i[1]])
            
        return result