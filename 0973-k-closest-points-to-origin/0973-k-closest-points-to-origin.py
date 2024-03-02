class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        
        for x, y in points:
            dist = x * x + y * y
            if len(pq) < k:
                heapq.heappush(pq, (-dist, x, y))
            else:
                heapq.heappushpop(pq, (-dist, x, y))
                
        res = [[x, y] for dist, x, y in pq]
        return res