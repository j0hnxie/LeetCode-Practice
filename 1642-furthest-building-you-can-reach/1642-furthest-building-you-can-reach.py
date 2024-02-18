class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        b = bricks
        
        pq = []
        for i in range(n - 1):
            cur = heights[i]
            nex = heights[i + 1]
            diff = nex - cur
            
            if diff > 0:
                heapq.heappush(pq, diff)
                
                if len(pq) > ladders:
                    low = heapq.heappop(pq)
                    b -= low
                # print(pq)
                # print(b)
                    
                if b < 0:
                    return i
        return n - 1